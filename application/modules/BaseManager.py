class BaseManager:
    def __init__(self, db, mediator, sio, MESSAGES):
        self.db = db
        self.mediator = mediator
        self.sio = sio
        self.MESSAGES = MESSAGES
        self.TRIGGERS = self.mediator.getTriggers()
        self.EVENTS = self.mediator.getEvents()
