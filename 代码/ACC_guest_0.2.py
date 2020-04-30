import socket
# import time
import pickle


class AC_Guest:

    # instance function
    def __init__(self, given_status, trigger):
        self.state = given_status      # current state of AC (on/off)
        self.switch = trigger          # indicates if user switched the state or not
        # self.temp = 30               # we will need these parts later
        # self.air_speed = 67

    # state switch
    def state_switch(status):
        if status == 1:
            status = 0
        else:
            status = 1
        return status

    # output
    def user_state_print(status):
        if status == 1:
            OnOffLabel = "ON"
        else:
            OnOffLabel = "OFF"
        print("The current state of the AC is " + OnOffLabel)

    # sends data
    def send_data(self, socket, trigger):
        data_to_send = [self.state]                 # create the list that contains the data from instance
        # data_to_send = [self.price, self.temp, self.air_speed]
        pickle_data = pickle.dumps(data_to_send)

        # if we press switch, only then the we send the data.
        if self.switch == 1:
            socket.send(pickle_data)
            # print("Signal sent")

        # This part is used for updating the stats every three seconds. I deactivated this part for now.
        # while True:
        #     time.sleep(3)
        #     socket.send(pickle_data)
        #     print("Sent with ease")

# implements input
def user_input():
    active_key=input("Enter A to SWITCH ")
    if active_key=='A':
        return 1
    else:
        return 0

def main():
    server = socket.socket()
    port = 1234
    server.connect(('127.0.0.1', port))
    # server.connect(('10.128.215.182', port))

    # initial status is 0
    IsOn=0
    while True:
        switch_command = user_input()
        initial_status = AC_Guest(IsOn, switch_command)
        AC_Guest.user_state_print(IsOn)
        if switch_command == 1:
            IsOn = AC_Guest.state_switch(IsOn)
        else:
            print("Fatal error, please restart")
        print("================================")

        AC_Guest.send_data(initial_status, server, switch_command)

    server.close()


if __name__ == '__main__':
    main()