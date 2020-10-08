from application.modules.BaseManager import BaseManager


class ChatManager(BaseManager):
    def __init__(self, db, mediator, sio):
        super().__init__(db, mediator, sio)

        @sio.event
        def onSendMessage(sid, data, room):
            self.sendMessage(sid, data, room)

        @sio.event
        def onSubscribeRoom(sid, data):
            self.subscribeRoom(sid, data['room'])

    async def sendMessage(self, sid, data):
        await self.__sio.emit('sendMessage', data)

    def subscribeRoom(self, sid, room):
        self.__sio.enter_room(sid, room)
