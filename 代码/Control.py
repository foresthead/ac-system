#for a better control and a good maintenance, the dispatch and services part are written in another .py files and been imported
import dispatch
import services



class control:

    def __init__(self):                     #生命并定义空调的基本数据
        self.mode = "low"
        self.Temp_highLimit = 30
        self.temp_lowLimit = 16
        self.default_TargetTemp = 23
        self.default_Feerate = 0.1
        self.Feerate_H = 0.1
        self.Feerate_M = self.Feerate_H + 0.1
        self.Feerate_L = self.Feerate_H - 0.1


    #初始化空调基本数据（风速，温度，费率，。。。）
    def setInitialValues(self):
        self.mode = input()
        self.Temp_highLimit = input()
        self.temp_lowLimit = input()
        self.default_TargetTemp = input()
        self.default_Feerate = input()
        self.Feerate_H = input()
        self.Feerate_M = input()
        self.Feerate_L = input()


    def PowerON(self):
        ServicesQueue = []
        ServicesQueue.append(services.services())
        ServicesQueue.append(services.services())
        ServicesQueue.append(services.services())
        Dispatch = dispatch.dispatch()
        #Dispatch.Initialization()

        return Dispatch, ServicesQueue

    def StartUp(self, Dispatch, ServicesQueue):
        Dispatch.ChangeState("Ready")
        ServicesQueue[0].ChangeState("Ready")
        ServicesQueue[1].ChangeState("Ready")
        ServicesQueue[2].ChangeState("Ready")


      
