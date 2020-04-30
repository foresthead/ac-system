import socket
import time
import pickle


class user:
    def __init__(self):
        self.price = 23.5
        self.temp = 30
        self.air_speed = 67

    def monitoring(self, socket):
        Data = [self.price, self.temp, self.air_speed]
        PickleData = pickle.dumps(Data)
        while True:
            time.sleep(3)
            socket.send(PickleData)
            print("Sent with ease")

def main():
    server = socket.socket()
    port = 1234
    #server.connect(('127.0.0.1', port))
    server.connect(('10.128.215.182', port))
    var = user()
    user.monitoring(var, server)
    server.close()


if __name__ == '__main__':
    main()
