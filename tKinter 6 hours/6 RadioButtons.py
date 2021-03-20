from tkinter import *
from PIL import ImageTk, Image
import os

# everything is a widget in tkinter. 
# 1st job is to make the 'root' widget which all other widgets sit in.
root = Tk()
root.title("Playing with Frames")
root.iconbitmap('caballo_icon.ico')

r = StringVar() # other options are IntVar()
r.set("Welcome to the Pizzaria")
# Use r.get() to access, not just 'r'

TOPPINGS = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, topping in TOPPINGS:
    Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)

def clicked( value ):
    myLabel = Label(root, text=value)
    myLabel.pack()

myLabel = Label(root, text=r.get())
myLabel.pack()

myButton = Button(root, text="Click me!", command = lambda: clicked(pizza.get()))
myButton.pack()

# the loop is essential in GUI programming. It allows the program to 'listen'
root.mainloop()
