#input function
def userKey():
    active_key=input("Enter A to SWITCH ")
    if active_key=='A':
        return 1
    else:
        return 0


#switch function
def OnOff_switch(status):
        if status==1:
            status=0
        else:
            status=1
        return status

#print current state
def state_print(status):
    if status == 1:
        OnOffLabel = "ON"
    else:
        OnOffLabel = "OFF"
    print("The current state of the AC is " + OnOffLabel)

IsOn=0
while True:
    state_print(IsOn)
    switch_command=userKey()
    if switch_command==1:
         IsOn=OnOff_switch(IsOn)
    else:
        print("ERROR")
    print("====================================")