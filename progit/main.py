import requests
from stop import Stop
from passing_time import PassingTime

api_base_url = 'https://us-central1-progit-playground.cloudfunctions.net'

# Fetch stops from AtB API and convert them into our own format
stops_url = api_base_url + '/stops'
stops_response = requests.get(stops_url)
stops_fetched = stops_response.json()['stops']

stops = {}
for stop_fetched in stops_fetched:
    id = stop_fetched['id']
    stops[id] = Stop(stop_fetched)

# Fetch passing times from AtB API and append them to the correct stop
passing_times_url = api_base_url + '/passingTimes'
passing_times_response = requests.get(passing_times_url)
passing_times_fetched = passing_times_response.json()['passingTimes']

for passing_time_fetched in passing_times_fetched:
    passing_time = PassingTime(passing_time_fetched)
    stop_id = passing_time.get_stop_id()
    # Discard the passing time if we don't have information about its stop
    if stop_id in stops:
        stops[stop_id].append_passing_time(passing_time)

# Print presentable timetables
for id in stops:
    stops[id].print_timetable()
    print()