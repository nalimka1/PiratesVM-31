import hashlib
import random

from application.modules.BaseManager import BaseManager


class UserManager(BaseManager):
    def __init__(self, db, mediator, sio):
        super().__init__(db, mediator, sio)
        # регистрируем триггеры
        self.mediator.set(self.TRIGGERS['GET_USER_BY_TOKEN'], self.__getUserByToken)
        self.mediator.set(self.TRIGGERS['GET_USER_BY_LOGIN'], self.__getUserByLogin)
        self.mediator.set(self.TRIGGERS['GET_HASH_BY_LOGIN'], self.__getHashByLogin)
        # регистрируем события
        self.mediator.subscribe(self.EVENTS['INSERT_USER'], self.__insertUser)
        self.mediator.subscribe(self.EVENTS['UPDATE_TOKEN_BY_LOGIN'], self.__updateTokenByLogin)

    def __generateToken(self, login):
        if login:
            randomInt = random.randint(0, 100000)
            return self.__generateHash(login, str(randomInt))

    def __generateHash(self, str1, str2=""):
        if type(str1) == str and type(str2) == str:
            return hashlib.md5((str1 + str2).encode("utf-8")).hexdigest()
        return None

    def __getUserByToken(self, data=None):
        if data:
            return self.__db.getUserByToken(data['token'])
        return None

    def __getUserByLogin(self, data):
        if data:
            return self.__db.getUserByLogin(data['login'])
        return None

    def __getHashByLogin(self, data):
        if data:
            return self.__db.getHashByLogin(data['login'])
        return None

    def __insertUser(self, data):
        if data:
            return self.__db.insertUser(data['name'], data['login'], data['password'], data['token'])
        return None

    def __updateTokenByLogin(self, data):
        if data:
            return self.__db.updateTokenByLogin(data['login'], data['token'])
        return None

    def registration(self, name, login, password):
        user = self.mediator.get(self.TRIGGERS['GET_USER_BY_LOGIN'], dict(login=login))
        if user or not name or not login or not password:
            return None
        else:
            password = self.__generateHash(password)
            token = self.__generateToken(login)
            self.mediator.call(self.EVENTS['INSERT_USER'], dict(name=name, login=login, password=password, token=token))
            return True

    def auth(self, login, hash, rnd):
        print(login, hash, rnd)
        if login and hash and rnd:
            hashDB = self.mediator.get(self.TRIGGERS['GET_HASH_BY_LOGIN'], dict(login=login))
            if self.__generateHash(hashDB, str(rnd)) == hash:
                token = self.__generateToken(login)
                self.mediator.call(self.EVENTS['UPDATE_TOKEN_BY_LOGIN'], dict(login=login, token=token))
                # добавляем пользователя в список пользователей онлайн
                self.mediator.call(self.EVENTS['ADD_USER_ONLINE'], dict(token=token))
                return True
        return False

    def logout(self, token):
        user = self.mediator.get(self.TRIGGERS['GET_USER_BY_TOKEN'],  dict(token=token))
        # удаляем пользователя из списка пользователей онлайн
        self.mediator.call(self.EVENTS['DELETE_USER_ONLINE'], dict(token=token))
        token = 'NULL'
        if user:
            self.mediator.call(self.EVENTS['UPDATE_TOKEN_BY_LOGIN'], dict(login=user['login'], token=token))
            return True
        return False
