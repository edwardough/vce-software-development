from tkinter import *
from PIL import ImageTk, Image
import os

# everything is a widget in tkinter. 
# 1st job is to make the 'root' widget which all other widgets sit in.
root = Tk()
root.title("Playing with Images")
root.iconbitmap('caballo_icon.ico')

# Just hit the 2 hour mark on YouTube FCC Tkinter in 5 hours

currPos = 0

my_img1 = ImageTk.PhotoImage(Image.open('runner1.png'))
my_img2 = ImageTk.PhotoImage(Image.open('runner2.png'))
my_img3 = ImageTk.PhotoImage(Image.open('runner3.png'))
my_img4 = ImageTk.PhotoImage(Image.open('runner4.png'))
my_img5 = ImageTk.PhotoImage(Image.open('runner5.png'))

# store all images in a list for easy iteration
image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

# create status bar information label
status = Label(root, text="Image " + str(currPos + 1) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

my_label = Label(image=image_list[0])
my_label.grid(row=0, column=0, columnspan=3)

def updateStatus( position ):
    global status # global retrieves the variable status from outside the function scope
    status.grid_forget()
    status = Label(root, text="Image " + str(currPos + 1) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def changeImage( direction ):
    global currPos
    global my_label
    global image_list

    if (currPos + direction) >= len(image_list):
        currPos = 0
    elif (currPos + direction) < 0:
        currPos = len(image_list) - 1
    else:
        currPos = currPos + direction
        
    updateStatus(currPos)
    my_label.grid_forget()
    my_label = Label(image=image_list[currPos])
    my_label.grid(row=0, column=0, columnspan=3)


button_back = Button(root, text="<<", command=lambda: changeImage(-1))
button_quit = Button(root, text="Exit", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: changeImage(1))

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

# the loop is essential in GUI programming. It allows the program to 'listen'
root.mainloop()