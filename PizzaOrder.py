def checkItem( item ):
    if item == 'h':
        print("Ham")
    elif item == 'p':
        print("Pepperoni")
    elif item == 'c':
        print("Cream")
    elif item == 'm':
        print("Marinara sauce")
    else:
        print("EXTRA CHEESE")

pizzaOrder = input("Order: ")

# Use a list structure to convert input into indiv
items = []
for char in pizzaOrder:
    items.append(char)
for i in items:
    checkItem(i)
