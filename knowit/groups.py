from group import Group
from event import Event

class Groups():
    def __init__(self):
        self.groups = []
        
    def add_group(self, name, type):
        self.groups.append(Group(name, type))
        return len(self.groups) - 1
        
    def get_group_by_id(self, group_id):
        return self.groups[group_id]
        
    def get_groups_by_type(self, type):
        returned_groups = []
        for group in self.groups:
            if group.type == 'Playground':
                returned_groups.append(group)
        return returned_groups
        
    def get_groups_with_events_with_at_least_n_participants(self, n):
        returned_groups = []
        for group in self.groups:
            for event in group.events:
                if event.max_participants >= n:
                    returned_groups.append(group)
                    break
        return returned_groups