import socket
import pickle


class AC_Manager:

    def __init__(self, given_status):
        self.state = given_status
        # self.temp = input("Enter the starting temperature:")
        # self.air_speed = input("Enter the starting air speed")

    # output
    def user_state_print(status):
        if status == 1:
            OnOffLabel = "ON"
        else:
            OnOffLabel = "OFF"
        print("The current state of the AC is " + OnOffLabel)

    def manager_state_print(status):
        if status == 1:
            OnOffLabel = "ON"
        else:
            OnOffLabel = "OFF"
        print("The current state of the AC is " + OnOffLabel)

    def data_recieve(self, socket):
        while True:
            # 4096 is used to pickle the data(can be revised)
            DataFromClient = socket.recv(4096)
            DataFromClient_decode = pickle.loads(DataFromClient)
            # print(DataFromClient_decode)
            print("this is the state:"+str(DataFromClient_decode[0]))
            # print("this is the temp:"+str(DataFromClient_decode[1]))
            # print("this is the airspeed:"+str(DataFromClient_decode[2]))

# implements input
def manager_input():
    active_key=input("Enter S to SWITCH ")
    if active_key=='S':
        return 1
    else:
        return 0

def main():
    server = socket.socket()
    port = 1234
    server.bind(('', port))
    server.listen()
    Client, addr = server.accept()
    if Client:
        print("Welcome to ACC Control System! The current state of AC is OFF")
        AC_Manager.data_recieve(AC_Manager, Client)
    print("the AC is turned off")



# this is the main function of the program
if __name__ == '__main__':
    main()