
# controller will tell classes what to do
class ReceptionController:
    def __init__(self, RDRorI, OutputType, RoomID):
        self.RDRorI = RDRorI  # this attribute will tell the class, what did user choose - invoice or DR
        self.OutputType = OutputType
        self.ID = RoomID
        self.ThisRDR = ServiceRDR(self.ID)
        self.ThisInvoice = ServiceRDR(self.ID)


    # this method is the constructor of RDR and invoice.
    def commandCreateList(self):
        if self.RDRorI == '1':
            print("RDR processing...")
            ListContent = self.ThisRDR.createList()
            self.Print(ListContent)
        elif self.RDRorI == '2':
            print("Invoice processing...")

        else:
            print("Processing error")



    # this method contains sends a printing command
    def Print(self, ListContent):
        self.ListContent = ListContent
        if self.RDRorI == '1':
            print("Printing DR...")
            Printer = RDRPrinter()
            if self.OutputType == '1':
                Printer.PutOnScreen(ListContent)
            elif self.OutputType == '2':
                Printer.PutInTxt(ListContent)
            else:
                print("Printer error")


        elif self.RDRorI == '2':
            print("Printing invoice...")

        else:
            print('print error')

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
        # datetime.datetime(2017, 4, 5, 0, 17, 8, 24239)
        TimeIn = self.ValuesSource.CheckInTime
        TimeNow = datetime.datetime.now()
        Duration = TimeNow - TimeIn
        result = [str(TimeIn), str(TimeNow), str(Duration)]
        return result



class RDRPrinter():
    def __init__(self):
        self.RoomID: int = RoomID

    def PutOnScreen(self, ListContent):
        for i in range(len(ListContent)):      # output every string of our list_RDR
            print(ListContent[i])

    def PutInTxt(self, ListContent):
        import webbrowser
        # for i in range(len(ListContent)):  # output every string of our list_RDR
        with open('detailed_record.txt', 'w') as printfile:
            for line in ListContent:
                printfile.write(line + '\n')
            # printfile.write(ListContent[i])
            webbrowser.open("detailed_record.txt")         #opening the reciept in notepad


class list_RDR:              # Gives us the PROPERLY FORMATTED LIST.
    def __init__(self, RoomID, prepareList):
        self.RoomID: int = RoomID
        self.prepareList = prepareList

    def ReadyList(self):
        prepareList = ServiceRDR(self.RoomID)
        prepareList.getValues()
        StringOne = str("Your room:\t\t\t" + self.RoomID)
        StringTwo = str("Temperature:\t\t" + self.prepareList[0])
        StringThree = str("FanSpeed:\t\t\t" + self.prepareList[1])
        StringFour = str("Fee Rate:\t\t\t" + self.prepareList[2])
        StringFive = str("Fee:\t\t\t\t" + self.prepareList[3])
        StringSix = ("Check In Time:\t\t" + self.prepareList[4])
        StringSeven = ("Time Now:\t\t" + self.prepareList[5])
        StringEight = ("Time in hotel:\t\t" + self.prepareList[6])
        result = [StringOne, StringTwo, StringThree, StringFour, StringFive, StringSix, StringSeven, StringEight]
        return result     # returns set of PROPERLY FORMATTED STRINGS.





##################################################################################
#                                                                                #
#                             INVOICE RELATED PART                               #
#                                                                                #
##################################################################################


class ServiceInvoice:
    print("Invoice Service running")
    pass


class InvoiceData:
    print("Invoice Data Gathered...")
    pass


class InvoicePrinter:
    print("Invoice Printer is on...")
    pass


##################################################################################
#                                                                                #
#                                    MAIN                                        #
#                                                                                #
##################################################################################


RDRorI = input("RDR or I (1 or 2)\n")
RoomID = input("Enter the room ID (1-5)\n")
OutputType: str = input("Show on the screen or Print (1 or 2)\n")
ReceptionQuery = ReceptionController(RDRorI, OutputType, RoomID)
ReceptionQuery.commandCreateList()
# if UserChoice == ('1'):
#     ReceptionQuery.Create_PrintList()
# elif UserChoice == ('2'):
#     ReceptionQuery.Print()
# else:
#     print("error")
