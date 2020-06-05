class waitingQueue:

    def __init__(self):
        self.queue = []


    def insert(self,request):
        #添加请求到等待队列
        self.queue.append(request)
        self.sort_by()
        print("the ", i, "th request is succefully inserted to the queue")


    def delete(self,request):
        #从等待队列删除请求
        for i in self.queue:
            if self.queue[i].id == request.id :
                self.queue.remove(self.queue[i])
        print("the ",i,"th request is succefully removed from the queue")


    def sort_by(self):
        #sort the queue according to the priority
        pass
