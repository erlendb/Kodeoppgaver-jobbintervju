from datetime import datetime, timedelta
import dateutil.parser
import pytz

class PassingTime():
    def __init__(self, fetched_information):
        self.id = fetched_information['id']
        self.stop_id = fetched_information['stopId']
        self.passing_time = fetched_information['passingTime']
        self.bus_code = fetched_information['busInfo']['publicCode']
        self.bus_name = fetched_information['busInfo']['displayName']
        
    def get_stop_id(self):
        return self.stop_id
    
    def print(self):
        # Convert the passing time into a readable format
        now = datetime.now(pytz.UTC)
        passing_time = dateutil.parser.parse(self.passing_time)
        time_difference = now - passing_time
        hours = int(time_difference.total_seconds() // 3600)
        minutes = int((time_difference.total_seconds() % 3600) / 60)
        if hours > 0:
            time_string = f'{hours}t {minutes}m'
        else:
            time_string = f'{minutes}m'
        
        print('(' + self.bus_code + ')', end = ' ')
        print(self.bus_name, end = ': ')
        print(time_string)