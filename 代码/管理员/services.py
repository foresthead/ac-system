
class services:

    def __init__(self):
        self.state = "Not Ready"
        self.Room_Id = 0
        self.mode = 0
        self.Temp_highLimit = 0
        self.temp_lowLimit = 0
        self.default_TargetTemp = 0
        self.default_Feerate = 0
        self.Feerate_H = 0
        self.Feerate_M = 0
        self.Feerate_L = 0
        self.currentTemp = 0
        self.windspeed = 0


    def Initialization(self, mode, Temp_highLimit, temp_lowLimit, default_TargetTemp,Feerate_H, Feerate_M, Feerate_L):
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


    def accept_Service(self,Room_id, mode, TargetTemp, currentTemp, windspeed):
        self.Room_Id = Room_id
        self.mode = mode
        self.TargetTemp = TargetTemp
        self.currentTemp = currentTemp
        self.windspeed = windspeed
        self.ChangeState("On_duty")


