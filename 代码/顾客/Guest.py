from manager import services
from server_part import servers
import datetime

class client:
    def __init__(self):
        self.state = 0
        self.target_temp = 0
        self.windSpeed = 0
        self.AcMode = 0
        self.RoomId = 0
        self.currentFee = 0
        self.buff_max_size = 1024
        self.currentTemp = 0

    def build_connection(self):
        host = 0
        port = 0
        connection = servers.server.build_server()
        servers.server.listen_from(connection, port, host)
        return connection


    def query(self, connection, query_form):
        if query_form == "allow":
            request = [self.RoomId, self.target_temp, self.windSpeed]
            servers.server.send_data(connection, request)
            self.state = "Running"


    def post_query(self, connection, post_query_form):
        servers.server.send_data(connection, post_query_form)
        received_data = servers.server.receive_input(connection, self.buff_max_size)
        return received_data


    def ChangeTargerTemp(self, input_Target, connection):
        self.target_temp = input_Target
        status = self.post_query(connection, "changeTemp")
        self.query(connection, status)


    def RequestOff(self,connection):
        status = self.post_query(connection, "PowerOff")
        servers.server.closeSocket(connection)


    def RequestFee(self, connection):
        status = self.post_query(connection, "Fees")
        self.query(connection, status)

    def RequestON(self, connection):
        status = self.post_query(connection, "PowerOn")
        self.query(connection, status)


    def huiwen(self):
        while True:
            time_schedule.one_min_count(time_schedule)
            #self.currentTemp -= 1
            print("Temp decreased")





#-------------------------------------------------------------------------------------#
#                                                                                     #
#     below is the time class it is made of three methods, feel free to change        #
#                         it according to your need                                   #
#-------------------------------------------------------------------------------------#


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

