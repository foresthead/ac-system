import socket
import pickle

class manager:

    def __init__(self):
        self.price = input("Enter the starting price:")
        self.temp = input("Enter the starting temperature:")
        self.air_speed = input("Enter the starting air speed")

    def monitoring(self,socket):

        while True:
            # 4096 is used to pickle the data(can be revised)
            DataFromClient = socket.recv(4096)
            DataFromClient_decode = pickle.loads(DataFromClient)
            print(DataFromClient_decode)
            print("this is the price:"+str(DataFromClient_decode[0]))
            print("this is the temp:"+str(DataFromClient_decode[1]))
            print("this is the airspeed:"+str(DataFromClient_decode[2]))



def main():
    server = socket.socket()
    port = 1234
    server.bind(('', port))
    server.listen()
    Client, addr = server.accept()
    if Client:
        print("the AC is turned on")
        manager.monitoring(manager, Client)
    print("the AC is turned off")



#this is the main function of the program
if __name__ == '__main__':
    main()





