import datetime

class time_schedule:

    #get the currenttime
    def getTime(self):
        return datetime.datetime.now()


    #loop for one minutes
    def one_min_count(self):
        current_time = datetime.datetime.now()
        increasing_time = self.getTime(time_schedule) - current_time
        while increasing_time.total_seconds() < 60:
            increasing_time = datetime.datetime.now() - current_time


    def time_difference(self, starting_time):
        return starting_time - datetime.datetime.now()

