class dispatch:
    def __init__(self):
        self.State = "not Ready"

    # def Initialization(self):

    def ChangeState(self, State):
        self.State = State

    def PrintState(self):
        print(self.State)
    # def GetRoomState(self):

