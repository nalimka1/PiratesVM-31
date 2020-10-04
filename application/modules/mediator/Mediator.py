class Mediator:
    EVENT_TYPES = {}
    TRIGGERS = {}
    events = {}
    triggers = {}

    def __init__(self, EVENT_TYPES, TRIGGERS):
        self.EVENT_TYPES = EVENT_TYPES
        self.TRIGGERS = TRIGGERS
        for key in self.EVENT_TYPES.keys():
            self.events.update({self.EVENT_TYPES[key]: []})

    def __del__(self):
        self.events.clear()
        self.triggers.clear()

    # TRIGGERS

    def getTriggers(self):
        return self.TRIGGERS

    def gettriggers(self):
        return self.triggers

    def set(self, name, func):
        if self.TRIGGERS.get(name) and func:
            self.triggers.update({name: func})

    def get(self, name, data=None):
        if name:
            cb = self.triggers.get(name)
            return cb(data)

    # EVENTS

    def getEventTypes(self):
        return self.EVENT_TYPES

    # подписаться на событие
    def subscribe(self, name, func):
        if name and func:
            self.events.update({self.events.get(name): func})

    # дернуть события (вызвать все колбеки, которые в него прописаны)
    def call(self, name, data=None):
        if name:
            cbs = self.events.get(name)
            if cbs:
                for cb in cbs:
                    cb(data)
