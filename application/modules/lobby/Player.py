class Player:
    def __init__(self, data):
        self.token = data['token']
        self.sid = data['sid']
        self.readyToStart = data['readyToStart'] if data['readyToStart'] else False
