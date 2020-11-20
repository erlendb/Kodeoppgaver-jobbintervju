from groups import Groups
from datetime import datetime

# Initiate the groups system
g = Groups()

# Test adding group
group_id = g.add_group('gruppe0', 'Playground')
print(g.groups[group_id].name, g.groups[group_id].type, g.groups[group_id].events)

# Test adding event to group
g.groups[group_id].add_event('21.10.20', 10, 'heisnn sveisann')
print(g.groups[group_id].name, g.groups[group_id].type, g.groups[group_id].events)
print(g.groups[group_id].events[0].date, g.groups[group_id].events[0].max_participants, g.groups[group_id].events[0].description)

# Test getting all events from group
print(g.groups[0].get_events())
print(g.groups[0].get_events()[0].date)

# Test getting groups by type
print(g.get_groups_by_type('Playground'))

# Test getting groups by id
print(g.get_group_by_id(group_id))

# Test find groups with events with more than n participants
print(len(g.get_groups_with_events_with_at_least_n_participants(10)))

# Test get future events
print(g.groups[0].get_future_events())

print()

# Test adding event in the past to group
g.groups[0].add_event('19.10.20', 10, 'heisnn sveisann')
print(g.groups[0].name, g.groups[0].type, g.groups[0].events)
print(g.groups[0].events[0].date, g.groups[0].events[0].max_participants, g.groups[0].events[0].description)
