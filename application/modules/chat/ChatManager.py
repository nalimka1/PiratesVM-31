from application.modules.BaseManager import BaseManager
from application.modules.game.Point import Point


class ChatManager(BaseManager):
    def __init__(self, db, mediator, sio, CHAT):
        super().__init__(db, mediator, sio)
        self.__CHAT = CHAT
        # массив из словарей dict(token=token, sid=sid)
        self.__usersSid = []
        self.__sid = ''
        # TODO
        # 1. ПРИДУМАТЬ ГДЕ ХРАНИТЬ КООРДИНАТЫ!!!
        # (Когда измените место хранения коородинат исправте метод sendMessageToEchoChat)

        # В массиве playersCoord должны храняться словари dict(token=token, point=Point(x, y))
        self.playersCoord = []

        self.mediator.subscribe(self.EVENTS['ADD_USER_ONLINE'], self.addUserOnline)
        self.mediator.subscribe(self.EVENTS['DELETE_USER_ONLINE'], self.deleteUserOnline)

        @sio.event
        def connect(sid, environ):
            self.__sid = sid
            print('connect ', sid)

        @sio.event
        def disconnect(sid):
            print('disconnect ', sid)

        @sio.on('sendMessage')
        async def onSendMessage(sid, data):
            if data['token']:
                await self.sendMessage(data)

        @sio.on('subscribeRoom')
        def onSubscribeRoom(sid, data):
            if data['token']:
                self.subscribeRoom(sid, data['room'])

    # отпрваить сообщение
    async def sendMessage(self, sid, data):
        if data['room']:
            await self.sio.emit('sendMessage', data, data['room'])
        else:
            await self.sio.emit('sendMessage', data)

    async def sendMessageToEchoChat(self, sid, data):
        room = 'echo'
        senderToken = None
        senderCoord = None
        for userSid in self.__usersSid:
            if userSid['sid'] == sid:
                senderToken = userSid['token']
                break
        for userCoord in self.playersCoord:
            if userCoord['token'] == senderToken:
                senderCoord = userCoord['point']
                break
        # подписываем пользователей находящихся на определённом расстоянии
        for userCoord in self.playersCoord:
            # Измеряем расстояние между двумя игроками
            distance = self.mediator.get(
                self.TRIGGERS['COUNT_DISTANCE'],
                dict(point1=senderCoord, point2=userCoord['point'])
            )
            if distance <= self.__CHAT['ECHO_DISTANCE']:
                for userSid in self.__usersSid:
                    if userSid['token'] == userCoord['token']:
                        self.subscribeRoom(userSid['sid'], room)
        # отправляем сообщение всем в комнате
        await self.sendMessage(sid, data)
        # удаляем всех подписчиков из комнаты
        for user in self.__usersSid:
            self.exitRoom(user['sid'], room)


    # подписаться на комнату
    def subscribeRoom(self, sid, room):
        self.sio.enter_room(sid, room)

    # отписаться от комнаты
    def exitRoom(self, sid, room):
        self.sio.leave_room(sid, room)

    # добавить пользователя в список подключённых
    def addUserOnline(self, data):
        if data and data['token']:
            self.__usersSid.append(dict(token=data['token'], sid=self.__sid))
            print(self.__usersSid)

    # удалить пользователя из списка подключённых
    def deleteUserOnline(self, data):
        if data and data['token']:
            for i in range(len(self.__usersSid)):
                if self.__usersSid[i].token == data['token']:
                    del self.__usersSid[i]
            print(self.__usersSid)
