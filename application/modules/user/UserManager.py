import hashlib
import random


class UserManager:
    def __init__(self, db, mediator):
        self.__db = db
        self.__mediator = mediator
        self.TRIGGERS = self.__mediator.getTriggers()
        # регистрируем триггеры и события
        self.__mediator.set(self.TRIGGERS['GET_USER_BY_TOKEN'], self.__getUserByToken)

    def __generateToken(self, login):
        if login:
            randomInt = random.randint(0, 100000)
            return self.__generateHash(login, str(randomInt))

    def __generateHash(self, str1, str2=""):
        if type(str1) == str and type(str2) == str:
            return hashlib.md5((str1 + str2).encode("utf-8")).hexdigest()
        return None

    def __getUserByToken(self, token=None):
        if token:
            return self.__db.getUserByToken(token)
        return None

    def registration(self, name, login, password):
        user = self.__db.getUserByLogin(login)
        if user or not name or not login or not password:
            return False
        token = self.__generateToken(login)
        self.__db.insertUser(name, login, password, token)
        return token

    def auth(self, login, hash, rnd):
        if login and hash and rnd:
            hashDB = self.__db.getHashByLogin(login)
            if self.__generateHash(hashDB, str(rnd)) == hash:
                token = self.__generateToken(login)
                self.__db.updateTokenByLogin(login, token)
                return token
        return False

    def logout(self, login):
        user = self.__db.getUserByLogin(login)
        if user:
            self.__db.updateTokenByLogin(login, "")
            return True
        return False

