import hashlib
import random


class Manager:
    def __init__(self, db):
        self.__db = db

    def registration(self, name, login, password):
        user = self.__db.getUserByLogin(login)
        if user or name is None or login is None or password is None:
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

    def __generateToken(self, login):
        if login:
            randomInt = random.randint(0, 100000)
            return self.__generateHash(login, str(randomInt))

    def __generateHash(self, str1, str2=""):
        if type(str1) == str and type(str2) == str:
            return hashlib.md5((str1 + str2).encode("utf-8")).hexdigest()
        return None
