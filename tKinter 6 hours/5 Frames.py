from tkinter import *
from PIL import ImageTk, Image

# everything is a widget in tkinter. 
# 1st job is to make the 'root' widget which all other widgets sit in.
root = Tk()
root.title("Playing with Frames")
root.iconbitmap('caballo_icon.ico')

frame = LabelFrame(root, text="This is my frame", padx=5, pady=5) # note the INTERNAL padding
frame.pack(padx=10, pady=10) # note this is EXTERNAL padding

my_button = Button(frame, text="Exit life", command=root.quit)
my_button.grid(row=0,column=0) # note that I can do a grid INSIDE a LabelFrame

# the loop is essential in GUI programming. It allows the program to 'listen'
root.mainloop()