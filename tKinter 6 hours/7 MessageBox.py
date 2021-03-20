from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

# everything is a widget in tkinter. 
# 1st job is to make the 'root' widget which all other widgets sit in.
root = Tk()
root.title("Learn to tKinter")
root.iconbitmap('caballo_icon.ico')
root.geometry("150x150")

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
# note they have different sound effects attached to each
def popup():
    response = messagebox.askyesno("This is a popup", "Popups are so annoying?")
    if response == False:
        Label(root, text="Uh yes they are!").pack()
    else:
        Label(root, text="Correct answer 1000 points").pack()


Button(root, text="Click on me!", command=popup).pack(anchor=W)
Button(root, text="Quit", command=root.quit).pack(anchor=W)

# the loop is essential in GUI programming. It allows the program to 'listen'
root.mainloop()