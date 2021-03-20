from tkinter import *
import time

# everything is a widget in tkinter. 
# 1st job is to make the 'root' widget which all other widgets sit in.
root = Tk()
root.title("Adding machine")

# set up the 'entry' widget
e = Entry(root, width=35)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


# Define functions
def button_click( number ):
    current = e.get() + str(number)
    e.delete(0,END)
    e.insert(0, current)

def button_clear():
    e.delete(0,END)

def button_add():
    global first_number
    first_number = e.get().lstrip("0")
    e.delete(0,END)
    e.insert(0, str(first_number) + " + ")

def button_equals():
    print("Debug: ", first_number)
    myExp = e.get()
    # TODO: Currently if there is a leading zero in the second part of the expression it crashes
    myExp = myExp.replace(",","") # prevents the commas from crashing the eval() statement below
    e.delete(0,END)
    try:
        e.insert(0, str(format(eval(myExp),",")))
    except:
        e.insert(0, "Invalid expression, clear & try again")

# Define buttons
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=39, pady=20, command=button_add) # Note: only use lambda functions if you need to pass a parameter
button_equal = Button(root, text="=", padx=89, pady=20, foreground='green', command=button_equals)
button_clear = Button(root, text="Clear", padx=79, pady=20, foreground='red',command=button_clear)

# Place buttons on screen
button_1.grid(row=3 ,column=0 )
button_2.grid(row=3 ,column=1 )
button_3.grid(row=3 ,column=2 )
button_4.grid(row=2 ,column=0 )
button_5.grid(row=2 ,column=1 )
button_6.grid(row=2 ,column=2 )
button_7.grid(row=1 ,column=0 )
button_8.grid(row=1 ,column=1 )
button_9.grid(row=1 ,column=2 )
button_0.grid(row=4 ,column=0 )
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

# the loop is essential in GUI programming. It allows the program to 'listen'
root.mainloop()