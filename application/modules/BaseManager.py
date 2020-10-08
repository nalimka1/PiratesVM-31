class BaseManager:
    def __init__(self, db, mediator, sio):
        self.__db = db
        self.__mediator = mediator
        self.__sio = sio
        self.__TRIGGERS = self.__mediator.getTriggers()
        self.__EVENTS = self.__mediator.getEvents()
