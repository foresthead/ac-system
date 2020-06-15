from Client import Guest
from manager import services
from server_part import servers

class control:
    def __init__(self):
        self.state = "Not Ready"
        self.available_services = 3
        self.service_in_run = 0
        self.services = []

        self.mode = 0
        self.Temp_highLimit = 0
        self.temp_lowLimit = 0
        self.default_TargetTemp = 0
        self.Feerate_H = 0
        self.Feerate_M = 0
        self.Feerate_L = 0


    def power(self):
        self.services.append(services.Services())
        self.services.append(services.Services())
        self.services.append(services.Services())
        #service = services.Services()
        dispatches = dispatch()
        return self.services, dispatches


    def StartUp(self, services, dispatch):
        for i in range(0,3):
            services[i].Initialization(self.mode, self.Temp_highLimit, self.temp_lowLimit, self.default_TargetTemp,
                                       self.Feerate_H, self.Feerate_M, self.Feerate_L)

        dispatch.Initialization(self.mode, self.Temp_highLimit, self.temp_lowLimit, self.default_TargetTemp,
                       self.Feerate_H, self.Feerate_M, self.Feerate_L)


    def create_waitingQueue(self):
        self.waitingQueue = waitingQueue()



class dispatch:
    def __init__(self):
        self.state = "Not ready"
        self.available_services = 3
        self.service_in_run = 0


    def changeState(self):
        if self.state == "Not Ready":
            self.state = "Ready"
        else :
            if self.state == "Ready":
                self.state = "Not Ready"


    def request_handling(self, services, connection, server, address):

        #if self.available_services < 3:
            #self.post_request_handler(connection, server, services)
        print(self.available_services)
        services[self.service_in_run].request_handler(connection, server, address)

        '''else :
            reqeust_to_switch = 0
            switch_status = 0
            print(self.available_services)
            #first check the priority
            request_to_switch, switch_status = self.check_by_priority(connection, services, server)
            if switch_status == "Yes":
                services[request_to_switch].switch_request()
                waitingQueue.insert_request(connection, address)
            else:
                waitingQueue.insert_request(connection, address)'''


    def Initialization(self, mode, Temp_highLimit, temp_lowLimit, default_TargetTemp,
                       Feerate_H, Feerate_M, Feerate_L):
        #初始化服务对象，注意state及Room_Id两个参数不要初始化。服务对象介绍一个请求后才能被初始化
        self.mode = mode
        self.Temp_highLimit = Temp_highLimit
        self.temp_lowLimit = temp_lowLimit
        self.default_TargetTemp = default_TargetTemp
        self.Feerate_H = Feerate_H
        self.Feerate_M = Feerate_M
        self.Feerate_L = Feerate_L
        self.state = "Ready"


    def check_by_priority(self, connection, services, server):
        data = server.receive_input(connection)
        state = "No"
        print(data)
        if data == "PowerOn":
            print("this is my request:" + data)
            server.send_data(connection, "allowed")
            request = server.receive_input(connection)
        for i in range(0,3):
            if request[1] > services[i].currentTemp:
                state = "Yes"
                return i, state
        if state == "no":
            return "null", state




class waitingQueue:
    def __init__(self):
        self.request = []
        self.queue = []


    def sort_by(self):
        pass


    def insert_request(self,connection,address,request):
        self.request[0] = str(address[0])
        self.request[1] = str(address[1])
        self.request[2] = connection
        self.request[3] = request
        self.request[4] = Guest.time_schedule.getTime(Guest.time_schedule())
        self.queue.append(self.request)
        
        
        
        
        
#services classe
#from Client import Guest
#from server_part import servers
#above package have to be imported or just copy to this file in order for the services class to work
import datetime


class Services:

    def __init__(self):
        self.state = "Not Ready"
        self.Room_Id = 0
        self.mode = 0
        self.Temp_highLimit = 0
        self.temp_lowLimit = 0
        self.TargetRoomTemp = 0
        self.default_Feerate = 0
        self.Feerate_H = 0
        self.Feerate_M = 0
        self.Feerate_L = 0
        self.currentRoomTemp = 0
        self.windspeed = 0
        #self.request = Guest.client.request()

        #room address
        self.Room_Ip = 0
        self.Room_Port = 0

        #time
        self.starting_time = 0
        self.Running_time = 0
        self.ending_time = 0


    def Initialization(self, mode, Temp_highLimit, temp_lowLimit, default_TargetTemp,
                       Feerate_H, Feerate_M, Feerate_L):
        #初始化服务对象，注意state及Room_Id两个参数不要初始化。服务对象介绍一个请求后才能被初始化
        self.mode = mode
        self.Temp_highLimit = Temp_highLimit
        self.temp_lowLimit = temp_lowLimit
        self.default_TargetTemp = default_TargetTemp
        self.Feerate_H = Feerate_H
        self.Feerate_M = Feerate_M
        self.Feerate_L = Feerate_L


    def ChangeState(self, State):
        self.state = State


    #介绍请求
    def accept_request(self, request):
        self.Room_Id = request.roomId
        self.mode = request.mode
        self.TargetTemp = request.TargetTemp
        self.currentTemp = request.currentTemp
        self.windspeed = request.windSpeed
        self.ChangeState("On_duty")
        self.starting_time = datetime.datetime.now()
        #return "accepted"


    def increase_roomTemp(self, connection):
        servers.server.send_data(connection, "updateTemp")
        if servers.server.receive_input() == "ready":
            servers.server.send_data(connection, self.currentTemp + 1)
            self.currentTemp += 1


    def decrease_roomTemp(self, connection):
        servers.server.send_data(connection, "updateTemp")
        if servers.server.receive_input() == "ready":
            servers.server.send_data(connection, self.currentTemp - 1)
            self.currentTemp -= 1


    def request_handler(self, connection, server, address):
        self.Room_Ip, self.Room_Port = str(address[0]), str(address[1])
        while True:
            data = server.receive_input(connection)
            print(data)
            if data == "PowerOn":
                print(self.Room_Ip ," is requesting to :" + data)
                #server.send_data(connection, "allowed")
                #request = server.receive_input(connection)
                #services

            else:
                if data == "changeTemp":
                    print(self.Room_Ip,"this is my request: " + data)
                    self.changeRoomTemp(request, connection)
                else:
                    if data == "PowerOff":
                        print(self.Room_Ip,"this is my request:" + data)
                        connection.close()
                        self.Running_time = 0
                        self.Room_fees = 0

                    else:
                        if data == "Fees":
                            print(self.Room_Ip,"this is my request:" + data)
                        else:
                            if data == "gao":
                                print(self.Room_Ip, "this is my request:" +data)
                                server.send(connection, "got it")



    def changeRoomTemp(self, request, connection):
        self.accept_request(request)
        if self.mode == "C":
            while self.currentRoomTemp < self.TargetRoomTemp:
                Guest.time_schedule.one_min_count()
                self.increase_roomTemp(connection)
        else:
            if self.mode == "H":
                while self.currentRoomTemp > self.TargetRoomTemp:
                    Guest.time_schedule.one_min_count()
                    self.decrease_roomTemp(connection)
