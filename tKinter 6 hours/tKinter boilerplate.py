from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

# everything is a widget in tkinter. 
# 1st job is to make the 'root' widget which all other widgets sit in.
root = Tk()
root.title("Learn to tKinter")
root.iconbitmap('caballo_icon.ico')
# root.geometry("250x150")



# the loop is essential in GUI programming. It allows the program to 'listen'
root.mainloop()