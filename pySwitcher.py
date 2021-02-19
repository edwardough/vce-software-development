def pySwitcher( choice ):
    # create a dictionary to match inputs with outputs
    switcher = {
        1: "Wheels up, captain!",
        2: "5 star accommodation for $5",
        3: "Ferrari or Lambo?",
        4: "The wheels on the bus go round and round"
    }
    # return the matched value to the given input
    return switcher.get( choice, "Invalid option" )

# print greeting
print("-- Book with us online! --")
print("[1] Flight")
print("[2] Hotel")
print("[3] Car")
print("[4] Bus")

# run program
uChoice = int(input("Enter your choice: "))
message = pySwitcher( uChoice )
print(message)

# exit gracefully
input('[ENTER] to end')
        
