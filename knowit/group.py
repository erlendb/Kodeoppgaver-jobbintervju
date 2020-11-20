from datetime import datetime
from event import Event

class Group():
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.events = []
        
    def add_event(self, date, max_participants, description):
        now = datetime.now()
        if datetime.strptime(date, '%d.%m.%y') >= now:
            self.events.append(Event(date, max_participants, description))
        else:
            return False
    
    def get_events(self):
        return self.events
        
    def get_future_events(self):
        now = datetime.now()
        future_events = []
        for event in self.events:
            if event.date < now:
                future_events.append(event)
        return future_events