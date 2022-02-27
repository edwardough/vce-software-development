from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

# everything is a widget in tkinter. 
# 1st job is to make the 'root' widget which all other widgets sit in.
root = Tk()
root.title("Learn to tKinter")
root.iconbitmap('caballo_icon.ico')
root.geometry("250x250")

vertical = Scale(root, from_=0, to=400)
vertical.pack() # note that pack has to be completed on its own line.

horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

def slider():
    root.geometry(str(horizontal.get())+"x"+str(vertical.get()))

btnUpdate = Button(root, text="Update window dimensions", command=slider).pack()
btnQuit = Button(root, text="Quit", command=root.quit).pack()

# the loop is essential in GUI programming. It allows the program to 'listen'
root.mainloop()