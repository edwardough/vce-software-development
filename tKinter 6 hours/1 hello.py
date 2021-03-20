from tkinter import *

# everything is a widget in tkinter. 1st job is to make the 'root' widget
root = Tk()

# creating anything in tkinter is a two step process.
# 1) create/define the thing
# 2) Display it / put it up on the screen

# label widgets can display text
myLabel = Label(root, text="Hello world!")

# pack is just like packing, shoving it in there in the first available spot. Unsophisticated.
myLabel.pack()

# the loop is essential in GUI programming
root.mainloop()


