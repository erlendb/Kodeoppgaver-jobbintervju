class Stop():
    def __init__(self, fetched_information):
        self.id = fetched_information['id']
        self.name = fetched_information['name']
        self.passing_times = []
        
    def append_passing_time(self, passing_time):
        self.passing_times.append(passing_time)
        
    def print_timetable(self):
        # Sort the passing_times array by passing time
        sorted_passing_times = sorted(self.passing_times, key=lambda i: i.passing_time, reverse = True)
        
        print(self.name)
        if len(sorted_passing_times) > 0:
            for passing_time in sorted_passing_times:
                passing_time.print()
        else:
            print('Ingen busser er på vei til dette stoppet')