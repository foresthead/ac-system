##################################################################################
#                                                                                #
#                             RDR RELATED PART                                   #
#                                                                                #
##################################################################################

# Reception controller for Requesting Detailed Records(RDR)
class RControlRDR:

    # this method creates RDRService class
    def CreateRDRService(self):
        print("object created")

    def CreateRDR(self):
        print("commanding to make RDR")

    def PrintRDR(self):
        print("passed the command to print")

class ServiceRDR:
    pass

class list_RDR:
    pass


##################################################################################
#                                                                                #
#                             INVOICE RELATED PART                               #
#                                                                                #
##################################################################################

class RControlInvoice:

    def CreateInvoiceService(self):
        print("invoice service created")

    def CreateInvoice(self):
        print("command to make invoice")

    def PrintInvoice(self):
        print("passed the command to print I")

class ServiceInvoice:
    pass

class InvoicePrinter:
    pass

class InvoiceData:
    pass

##################################################################################
#                                                                                #
#                                    MAIN                                        #
#                                                                                #
##################################################################################

controller1 = RControlRDR()
controller2 = RControlInvoice()
UserChoice = input("RDR or I")
if UserChoice == ('RDR'):
    UserChoice = input("1 2 or 3")
    if UserChoice==('1'):
        controller1.CreateRDRService()
    elif UserChoice==('2'):
        controller1.CreateRDR()
    elif UserChoice==('3'):
        controller1.PrintRDR()
    else:
        print("error")

if UserChoice == ('I'):
    UserChoice = input("1 2 or 3")
    if UserChoice==('1'):
        controller2.CreateInvoiceService()
    elif UserChoice==('2'):
        controller2.CreateInvoice()
    elif UserChoice==('3'):
        controller2.PrintInvoice()
    else:
        print("error")
