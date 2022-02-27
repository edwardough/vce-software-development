from tkinter import *

# everything is a widget in tkinter. 1st job is to make the 'root' widget
root = Tk()

# creating anything in tkinter is a two step process.
# 1) create/define the thing
# 2) Display it / put it up on the screen

# label widgets can display text
myLabel1 = Label(root, text="Hello world!")
myLabel2 = Label(root, text="My label 2 is about the booey")

# grid allows finer control over where things are placed on the screen.
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=1)

# note you can do this in one step, but is it cleaner?
myLabel3 = Label(root, text="Label 3 is about the baba").grid(row=2,column=2)

# the loop is essential in GUI programming. It allows the program to 'listen'
root.mainloop()


