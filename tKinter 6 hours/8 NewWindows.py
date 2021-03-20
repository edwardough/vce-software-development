from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

# everything is a widget in tkinter. 
# 1st job is to make the 'root' widget which all other widgets sit in.
root = Tk()
root.title("Learn tKinter")
root.iconbitmap('caballo_icon.ico')
root.geometry("250x150")

def openWindow():
    # often Python will treat variables inside functions as garbage to be collected
    # so sometimes a global declaration is required.
    global my_img
    top = Toplevel()
    top.title("An image")
    top.iconbitmap('caballo_icon.ico')
    my_img = ImageTk.PhotoImage(Image.open("Viewer\\runner1.png"))
    my_lbl = Label(top, image=my_img).pack()
    Button(top, text="Close window", command=top.destroy).pack() # note the destroy command - don't use quit

Button(root, text="Open new window", command=openWindow).pack()
Button(root, text="Quit program", command=root.quit).pack()


# the loop is essential in GUI programming. It allows the program to 'listen'
root.mainloop()