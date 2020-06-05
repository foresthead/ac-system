class dispatch:
    def __init__(self):
        self.State = "Not Ready"

    def ChangeState(self, State):
        self.State = State

    #客户端发个请求后，判断该请求是否分配服务对象还是放入等待队列
    def dispatch(self, services, waitingQueue, request):

        result = 1
        for i in range(0,3):
            #查看哪一个服务对象还没介绍请求
            if services.state == "Ready":
                services[i].accept_Service(request)
                print("the ", request.id," request was given to ", i," service")
                result = 1

        #没找到不忙的服务对象，把请求放入到等待队列
        if result != 0:
            waitingQueue.insert(request)
            print("Request ",request.id," succesfully inserted in the waitingQueue")

