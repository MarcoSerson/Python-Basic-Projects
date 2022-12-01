from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")

def clock():
    horario = strftime("%H:%M:%S")
    label.config(text=horario)
    label.after(1000, clock)

label = Label(root, font=("Helvetica", 60), background="#000", foreground="#00FF04")
label.pack(anchor="center")

clock()

mainloop()
