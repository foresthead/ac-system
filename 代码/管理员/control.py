import dispatch
import services



class control:

    def __init__(self):                     #生命并定义空调的基本数据
        self.state = "Not Ready"
        self.mode = "low"
        self.Temp_highLimit = 0
        self.temp_lowLimit = 0
        self.default_TargetTemp = 0
        self.default_Feerate = 0
        self.Feerate_H = 0
        self.Feerate_M = self.Feerate_H + 0.1
        self.Feerate_L = self.Feerate_H - 0.1


    def PowerON(self):
        ServicesQueue = []
        #创建三个服务对象
        ServicesQueue.append(services.services())
        ServicesQueue.append(services.services())
        ServicesQueue.append(services.services())
        Dispatch = dispatch.dispatch()
        #Dispatch.Initialization()
        return Dispatch, ServicesQueue


    #初始化空调基本数据（风速，温度，费率，。。。）
    def setPara(self, mode, Temp_highLimit, temp_lowLimit, default_TargetTemp,Feerate_H, Feerate_M, Feerate_L, ServicesQueue):
        #从用户得到初始参数
        self.mode = mode
        self.Temp_highLimit = Temp_highLimit
        self.temp_lowLimit = temp_lowLimit
        self.default_TargetTemp = default_TargetTemp
        self.Feerate_H = Feerate_H
        self.Feerate_M = Feerate_M
        self.Feerate_L = Feerate_L
        #初始化每个服务对象
        for i in range(0,3):
            ServicesQueue[i].Initialization(mode, Temp_highLimit, temp_lowLimit, default_TargetTemp,
                                            Feerate_H, Feerate_M, Feerate_L)


    def StartUp(self, Dispatch, ServicesQueue):

        if self.state == "Not Ready":
            # 启动后把服务对象及调度对象设置为 "Ready"
            Dispatch.ChangeState("Ready")
            ServicesQueue[0].ChangeState("Ready")
            ServicesQueue[1].ChangeState("Ready")
            ServicesQueue[2].ChangeState("Ready")
            self.state = "Ready"
            return "Ready"
        else :
            return "Error"

