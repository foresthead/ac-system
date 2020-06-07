#控制对象
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
        ServicesQueue.append(services())
        ServicesQueue.append(services())
        ServicesQueue.append(services())
        dispatch = Dispatch()
        print("successfuly powered on")
        return dispatch, ServicesQueue


    #初始化空调基本数据（风速，温度，费率，。。。）
    def setPara(self, ServicesQueue):
        data_location = input("would you like to keep the previous default values? Y/N")
        if data_location == 'Y':
            pass
        else :
            #从用户得到初始参数
            self.mode = input("set the default mode")
            self.Temp_highLimit = input("set the default Hight Limit for the temp")
            self.temp_lowLimit = input("set the default Low Limit for the temp")
            self.default_TargetTemp = input("set the default temp")
            self.Feerate_H = input("set the default fee rate for the Highest windspeed")
            self.Feerate_M = input("set the default fee rate for the Medium windspeed")
            self.Feerate_L = input("set the default fee rate for the Lowest windspeed")
        #初始化每个服务对象
        for i in range(0,3):
            ServicesQueue[i].Initialization(self.mode, self.Temp_highLimit, self.temp_lowLimit, self.default_TargetTemp,
                                            self.Feerate_H, self.Feerate_M, self.Feerate_L)


    def StartUp(self, Dispatch, ServicesQueue):

        if self.state == "Not Ready":
            # 启动后把服务对象及调度对象设置为 "Ready"
            Dispatch.ChangeState("Ready")
            ServicesQueue[0].ChangeState("Ready")
            ServicesQueue[1].ChangeState("Ready")
            ServicesQueue[2].ChangeState("Ready")
            self.state = "Ready"
            Dispatch.PrintState()
            ServicesQueue[0].PrintState()
            ServicesQueue[1].PrintState()
            ServicesQueue[2].PrintState()
            #server = servers.server()
            #server.start(Dispatch, ServicesQueue)
            return "Ready"
        else :
            return "Error"







#调度对象
class Dispatch:
    def __init__(self):
        self.State = "Not Ready"

    def ChangeState(self, State):
        self.State = State

    def PrintState(self):
        print(self.State)

    #客户端发个请求后，判断该请求是否分配服务对象还是放入等待队列
    def control(self, services, waitingQueue, request):

        result = 1
        for i in range(0,3):
            #查看哪一个服务对象还没介绍请求
            if services.state == "Ready":
                services[i].accept_Service(request)
                print("the ", request[0]," request was given to ", i," service")
                result = 1

        #没找到不忙的服务对象，把请求放入到等待队列
        if result != 0:
            waitingQueue.insert(request)
            print("Request ",request.id," succesfully inserted in the waitingQueue")










#服务对象
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
        print("service initialize with the default value")


    def ChangeState(self, State):
        self.state = State


    def PrintState(self):
        print(self.state)


    #介绍请求
    def accept_Service(self,request):
        self.Room_Id = request.Room_id
        self.mode = request.mode
        self.TargetTemp = request.TargetTemp
        self.currentTemp = request.currentTemp
        self.windspeed = request.windspeed
        self.ChangeState("On_duty")





#main函数可以随时改
def main():
    Control = control()
    dispatch , queue = Control.PowerON()
    Control.setPara(queue)
    Control.StartUp(dispatch, queue)
    print(Control.Temp_highLimit)
    #Control.StartUp(dispatch, queue)


if __name__ == '__main__':
    main()
