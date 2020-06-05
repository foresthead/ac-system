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


            
 
class waitingQueue:

    def __init__(self):
        self.queue = []
        self.queue_length = 0


    def insert(self,request):
        #添加请求到等待队列
        self.queue.append(request)
        self.queue_length += 1
        self.sort_by()
        print("the request ", request.id, " is succefully inserted to the queue")


    def delete(self,request):
        #从等待队列删除请求
        for i in self.queue:
            if self.queue[i].id == request.id :
                self.queue.remove(self.queue[i])
        print("the ",i,"th request is succefully removed from the queue")


    def sort_by(self):
        #sort the queue according to the priority
        pass
