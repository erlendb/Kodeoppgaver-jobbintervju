from datetime import datetime

class Event():
    def __init__(self, date, max_participants, description):
        self.date = datetime.strptime(date, '%d.%m.%y')
        self.max_participants = max_participants
        self.description = description