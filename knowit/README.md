# Reference

## The `Groups` class
This is the main class in the system.

### `groups`
A list of groups. Each group is an instance of the `Group` class.

### `__init__()`
Initiate the groups system, with an empty groups list.

### `add_group( name, type )`
Add a new group to the `Groups` instance. Returns the new group id.

### `get_group_by_id( group_id )`
Get the group with id `group_id` from the `Groups` istance.

### `get_groups_by_type( type )`
Returns a list with the groups of the given type.

### `get_groups_with_events_with_at_least_n_participants( n )`
Returns a list with the groups that have at least one event with at leat `n` participants. The events can be in the past or in the future.

## The `Groups` class

### `name`
Name of the group.

### `type`
The group type.

### `events`
A list of events in the group. Each event is an instance of the `Event` class.

### `__init__( name, type )`
Initiate a group with name, type, and an empty events list.

### `add_event( date, max_participants, description )`
Add an event to the group, given that the date is in the future.
Returns `False` if the event is not added.

### `get_events()`
Return a list of all events in the group, past or future.

### `get_future_events()`
Return a list of all future events in the group.

## The `Event` class

### `date`
The date of the event. This is a datetime object.

### `max_participants`
Maximum participants allowed to attend to the event.

### `desciption`
Description of the event.

### `__init__( date, max_participants, description )`
Initiates an event. The `date` argument must be on the form `dd.mm.yy`, e.g. `10.02.20`.