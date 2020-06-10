from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ReceptionMenu import Ui_MainWindowR

# RDR is Request Detail Records == 详单
# Invoice == 账单


# controller will tell classes what to do AND NOW it's also printing values

class ReceptionController:
    def __init__(self, RDRorI, OutputType, RoomID):
        self.RDRorI = RDRorI  # this attribute will tell the class, what did user choose - invoice or DR
        self.OutputType = OutputType
        self.ID = RoomID
        self.ThisRDR = ServiceRDR(self.ID)
        self.ThisInvoice = ServiceInvoice(self.ID)


    # this method is the constructor of RDR and invoice.
    def commandCreateList(self):
        if self.RDRorI == '1':
            print("RDR processing...")
            RDRContent = self.ThisRDR.createList()
            self.Print(RDRContent)
        elif self.RDRorI == '2':
            print("Invoice processing...")
            InvoiceContent = self.ThisInvoice.createInvoiceData()
            self.Print(InvoiceContent)
        else:
            print("Processing error")


    # this method contains sends a printing command
    def Print(self, ListContent):
        self.ListContent = ListContent
        if self.RDRorI == '1':
            print("Printing DR...")
            print("Printing DR...")
            if self.OutputType == '1':
                self.PutOnScreen(ListContent)
            elif self.OutputType == '2':
                self.PutInTxt(ListContent)
            else:
                print("Printer error")

        elif self.RDRorI == '2':
            print("Printing invoice...")
            if self.OutputType == '1':
                self.PutOnScreen(ListContent)
            else:
                print("Printer error")
        else:
            print('print error')

    # These methods USED TO BE a part of a printer class. But it's not working with GUI I don't know why

    def PutOnScreen(self, ListContent):
        # ui.textBrowser.setText(ListContent)
        for i in range(len(ListContent)):  # output every string of our list_RDR
            # print(ListContent[i])
            ui.textBrowser.append(ListContent[i])
        ui.textBrowser.append("=================================")

    def PutInTxt(self, ListContent):
        import webbrowser
        with open('detailed_record.txt', 'w') as printfile:
            for line in ListContent:
                printfile.write(line + '\n')
            webbrowser.open("detailed_record.txt")



class Database:
    def __init__(self):
        import datetime
        self.FanSpeed = 1
        self.FeeRate = 5
        self.Temperature = 28
        self.CheckInTime = datetime.datetime(2017, 2, 26)
        self.Fee = self.FanSpeed * self.FeeRate * (self.Temperature - 25)

##################################################################################
#                                                                                #
#                             RDR RELATED PART                                   #
#                                                                                #
##################################################################################


class ServiceRDR:   # This class made for creating DR that we can output on screen or print to file.
    def __init__(self, ID):
        self.RoomID: int = ID
        self.ValuesSource = Database()

    # taking values using getValues, putting them to list_RDR where they are properly formatted
    def createList(self):
        prepareList = self.getValues()
        ThisList = list_RDR(self.RoomID, prepareList)
        OutputScreen = ThisList.ReadyList()
        return OutputScreen


    # Getting values from Database and time method
    def getValues(self):
        OurTimeList = self.getRequestDuration()
        OurTemperature = self.ValuesSource.Temperature
        OurFanSpeed = self.ValuesSource.FanSpeed
        OurFeeRate = self.ValuesSource.FeeRate
        OurFee = self.ValuesSource.Fee
        OurDateIn = OurTimeList[0]
        OurDateOut = OurTimeList[1]
        OurDuration = OurTimeList[2]
        result = [str(OurTemperature), str(OurFanSpeed), str(OurFeeRate), str(OurFee), OurDateIn, OurDateOut, OurDuration]
        return result


    # does everything related to time and puts it in special list
    def getRequestDuration(self):
        import datetime
        TimeIn = self.ValuesSource.CheckInTime
        TimeNow = datetime.datetime.now()
        Duration = TimeNow - TimeIn
        result = [str(TimeIn), str(TimeNow), str(Duration)]
        return result





class list_RDR:              # Gives us the PROPERLY FORMATTED LIST.
    def __init__(self, RoomID, prepareList):
        self.RoomID: int = RoomID
        self.prepareList = prepareList

    def ReadyList(self):
        prepareList = ServiceRDR(self.RoomID)
        prepareList.getValues()
        StringOne = str("Your room:\t\t" + self.RoomID)
        StringTwo = str("Temperature:\t\t" + self.prepareList[0])
        StringThree = str("FanSpeed:\t\t" + self.prepareList[1])
        StringFour = str("Fee Rate:\t\t" + self.prepareList[2])
        StringFive = str("Fee:\t\t" + self.prepareList[3])
        StringSix = ("Check In Time:\t" + self.prepareList[4])
        StringSeven = ("Time Now:\t" + self.prepareList[5])
        StringEight = ("Time in hotel:\t" + self.prepareList[6])
        result = [StringOne, StringTwo, StringThree, StringFour, StringFive, StringSix, StringSeven, StringEight]
        return result     # returns set of PROPERLY FORMATTED STRINGS.





##################################################################################
#                                                                                #
#                             INVOICE RELATED PART                               #
#                                                                                #
##################################################################################


class ServiceInvoice:
    def __init__(self, ID):
        self.RoomID: int = ID
        self.ValuesSource = Database()

    def createInvoiceData(self):
        import datetime
        TimeIn = str(self.ValuesSource.CheckInTime)
        TimeNow = str(datetime.datetime.now())
        OurFee = str(self.ValuesSource.Fee)
        ThisList = InvoiceData(self.RoomID, TimeIn, TimeNow, OurFee)
        OutputScreen = ThisList.ReadyList()
        return OutputScreen


class InvoiceData:
    def __init__(self, RoomID, TimeIn, TimeNow, OurFee):
        self.RoomID: int = RoomID
        self.TimeIn = TimeIn
        self.TimeNow = TimeNow
        self.OurFee = OurFee

    def ReadyList(self, ):
        StringOne = str("Your room:\t" + self.RoomID)
        StringTwo = ("Check In Time:\t" + self.TimeIn)
        StringThree = ("Time Now:\t" + self.TimeNow)
        StringFour =  ("Fee:\t" + self.OurFee)
        result = (StringOne, StringTwo, StringThree, StringFour)
        return result


##################################################################################
#                                                                                #
#                                    MAIN                                        #
#                                                                                #
##################################################################################
def UiRdrInput():
    RDRorI = '1'
    OutputType = '1'
    RoomID = str(ui.spinID.value())
    print(RDRorI, OutputType, RoomID)
    ReceptionQuery = ReceptionController(RDRorI, OutputType, RoomID)
    ReceptionQuery.commandCreateList()

def UiInvoiceInput():
    RDRorI = ('2')
    OutputType = ('1')
    RoomID = str(ui.spinID.value())
    print(RDRorI, OutputType, RoomID)
    ReceptionQuery = ReceptionController(RDRorI, OutputType, RoomID)
    ReceptionQuery.commandCreateList()

if __name__ == "__main__":
            # create the app
            app = QtWidgets.QApplication(sys.argv)

            #create the form and init UI
            MainWindowR = QtWidgets.QMainWindow()
            ui = Ui_MainWindowR()
            ui.setupUi(MainWindowR)
            MainWindowR.show()

            #create hook logic
            ui.RDRbutton.clicked.connect(UiRdrInput)
            ui.InvoiceButton.clicked.connect(UiInvoiceInput)

            #run main loop
            sys.exit(app.exec_())

# RDR - Detailed Records(详单); I - invoice(账单)
# RDRorI = input("RDR or I (1 or 2)\n")
# RoomID = input("Enter the room ID (1-5)\n")
# if RDRorI == '1':
#     OutputType: str = input("Show on the screen or Print (1 or 2)\n")
# elif RDRorI == '2':
#     OutputType = '1'
# ReceptionQuery = ReceptionController(RDRorI, OutputType, RoomID)
# ReceptionQuery.commandCreateList()
