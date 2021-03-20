from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

# everything is a widget in tkinter. 
# 1st job is to make the 'root' widget which all other widgets sit in.
root = Tk()
root.title("Learn to tKinter")
root.iconbitmap('caballo_icon.ico')
# root.geometry("250x150")

def show():
    lblDemo = Label(root, text=var.get()).pack()

var = StringVar()

cbDemo = Checkbutton(root, text="Ho ho ho!", variable=var, onvalue="On", offvalue="Off")
cbDemo.deselect() # prevents some weird bugs
cbDemo.pack()

btnRandom = Button(root, text="Print selection", command=show).pack()

# the loop is essential in GUI programming. It allows the program to 'listen'
root.mainloop()