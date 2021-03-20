from tkinter import *

# everything is a widget in tkinter. 1st job is to make the 'root' widget
root = Tk()

def myClick():
  myLabel1 = Label(root, text="You clicked me! Wowzers", fg="green")
  myLabel1.pack()

myButton1 = Button(root, text="Click me!", state=DISABLED, padx = 50, pady = 20, fg="blue", bg="red")
myButton1.pack()

# note the weird tKinter behaviour here
# state = NORMAL instead of ENABLED
# command = myClick instead of myClick()
myButton2 = Button(root, text="Clickity click!", state=NORMAL, command=myClick)
myButton2.pack()

# the loop is essential in GUI programming. It allows the program to 'listen'
root.mainloop()


