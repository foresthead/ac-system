# controller will tell classes what to do


class ReceptionController:
    def __init__(self, InitialType):
        self.choice = InitialType  # this attribute will tell the class, what did user choose - invoice or DR

    # this method contains service constructor
    def CreateService(self):
        if self.choice == 'RDR':
            print("RDR service start...")
        elif self.choice == 'I':
            print("Invoice service start...")
        else:
            print("Service initializing error")

    # this method will create this object
    def Create_PrintList(self):
        if self.choice == 'RDR':
            print("RDR processing...")
        elif self.choice == 'I':
            print("Invoice processing...")
        else:
            print("Processing error")

    # this method contains sends a printing command
    def Print(self):
        if self.choice == 'RDR':
            print("Printing DR...")
        elif self.choice == 'I':
            print("Printing invoice...")
        else:
            print('print error')


##################################################################################
#                                                                                #
#                             RDR RELATED PART                                   #
#                                                                                #
##################################################################################


class ServiceRDR:
    pass


class list_RDR:
    pass


##################################################################################
#                                                                                #
#                             INVOICE RELATED PART                               #
#                                                                                #
##################################################################################


class ServiceInvoice:
    pass


class InvoiceData:
    pass


class InvoicePrinter:
    pass


##################################################################################
#                                                                                #
#                                    MAIN                                        #
#                                                                                #
##################################################################################


InitialType = input("RDR or I")
ReceptionQuery = ReceptionController(InitialType)
ReceptionQuery.CreateService()
UserChoice: str = input("Show on the screen or Print(1 or 2)")
if UserChoice == ('1'):
    ReceptionQuery.Create_PrintList()
elif UserChoice == ('2'):
    ReceptionQuery.Print()
else:
    print("error")
