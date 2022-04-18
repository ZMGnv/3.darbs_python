"""
Uzrakstiet programmu Python, 
lai parādītu pašreizējo datumu un laiku.
"""
from tkinter import *
from tkinter.ttk import *

from time import strftime

plkst = Tk()
plkst.title("Clock")
plkst.geometry('600x150')
def time():
    string = strftime("%H:%M:%S %p")
    label.config(text = string)
    label.after(1000, time)

label = Label(plkst, font = "ds-digital 100", background = "black", foreground = "cyan")
label.pack(anchor = "sw")
time()
mainloop()
