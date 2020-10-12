class BaseManager:
    def __init__(self, db, mediator, sio):
        self.db = db
        self.mediator = mediator
        self.sio = sio
        self.TRIGGERS = self.mediator.getTriggers()
        self.EVENTS = self.mediator.getEvents()
