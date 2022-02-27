from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
import os

# everything is a widget in tkinter. 
# 1st job is to make the 'root' widget which all other widgets sit in.
root = Tk()
root.title("Learn to tKinter")
root.iconbitmap('caballo_icon.ico')
# root.geometry("250x150")

# define functions
def chooseImage():
    global my_image
    root.filename =  filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select file",filetypes = (("png files","*.png"),("all files","*.*")))
    Label(root, text=root.filename).grid(row=3, column=0, sticky=W)
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_box = Label(image=my_image).grid(row=2, column=0)
    quitButton = Button(root, text="Quit", command=root.quit).grid(row=0, column=0, sticky=W)
    chooseButton = Button(root, text="Choose image", command=chooseImage).grid(row=1, column=0, sticky=W)

quitButton = Button(root, text="Quit", command=root.quit).grid(row=0, column=0, sticky=W)
chooseButton = Button(root, text="Choose image", command=chooseImage).grid(row=1, column=0, sticky=W)

# the loop is essential in GUI programming. It allows the program to 'listen'
root.mainloop()