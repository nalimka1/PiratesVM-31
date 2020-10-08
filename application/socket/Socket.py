class Socket:
    def __init__(self, sio, mediator):
        @sio.event
        def connect(sid, environ):
            print('connect', sid)

        @sio.event
        def disconnect(sid):
            print('disconnect', sid)

        @sio.event
        async def sendMessage(sid, data):
            sio.enter_room(sid, 'chat_users')
            sio.leave_room(sid, 'chat_users')
            await sio.emit('sendMessage', data, skip_sid=sid)
