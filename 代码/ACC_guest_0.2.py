import tkinter as tk
from tkinter import ttk
from tkinter import Listbox

#create the main window
win = tk.Tk()
win.geometry("450x500")
win.title("BUPT酒店")
win.resizable(0, 0)


#Adding the action to the click
'''def click_me():
    action.configure(text='hello ' + name.get())

def ChangeTextColor():
    a_labbel.configure(foreground = name.get())
'''

#changing the Label
#a_labbel = ttk.Label(win, text="Enter a name:")
#a_labbel.grid(column = 0, row = 0)


#Adding a Text box Entry widget, grid() is to set the position of the self.instance
'''name = tk.StringVar()
entered_name = ttk.Entry(win, width = 12, textvariable = name)
entered_name.grid(column = 0, row = 1)


#Adding a button , grid()is to set the position of the self.instance
action = ttk.Button(win, text = "Click Me!", command = click_me)
action.grid(column = 0, row = 2)

action2 = ttk.Button(win, text = "Change the text color", command = ChangeTextColor)
action2.grid(column = 1, row =1)
'''

#define the main windown
display_area = Listbox(win, height = 20, width = 74)
display_area.grid(row = 0, column = 0, columnspan = 4)

a_label = ttk.Label(win, text = "option")
a_label.grid(row = 1, column = 1, columnspan = 2)

#defining all the buttons
AirSpeed_up = ttk.Button(win, text = "Speed Up", command = "#")
AirSpeed_up.grid(row = 2, column = 0)

AirSpeed_down = ttk.Button(win, text = "Speed Down", command = "#")
AirSpeed_down.grid(row = 2, column = 1)

Temp_up = ttk.Button(win, text = "Temp Up", command = "#")
Temp_up.grid(row = 2, column = 2)

Temp_down = ttk.Button(win, text = "Temp Down", command = "#")
Temp_down.grid(row = 2, column = 3)

PowerButton = ttk.Button(win, text = "Power")
PowerButton.grid(row = 3, column = 3, rowspan = 2)


#this has to come at last
win.mainloop()
print(name.get())

