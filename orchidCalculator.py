import math
import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s -  %(message)s')
# logging.disable() 

priceList = {
    'V' : 7.35, # vandas
    'M' : 9.80, # miltonia
    'C' : 10.00 # cattleya
}

while True:
    member = input("Are you a member? [Y] or [N] > " )
    if member.upper() == 'Y':
        member = True
        break
    elif member.upper() == 'N':
        member = False
        break
    else:
        print("Please enter Y or N")

while True:
    orchid = input("Which Orchid would you like? [V]andas, [M]iltonia, or [C]attleya > ")
    if orchid.upper() not in ['V','M','C']:
        print("Please enter V, M or C")
    else:
        break

logging.debug("Member status > " + str(member))
logging.debug("Chosen orchid > " + str(orchid))

while True:
    try:
        quantity = int(input("How many do you want? > "))
        # if quantity not in range(0,100):
        if quantity < 0 or quantity > 100:
            print("Please enter a value between 1 and 99")
        else:
            price = quantity * priceList[orchid]
            logging.debug("Pre discount price > " + str(price))
            if member == True:
                # apply member discount
                price *= 0.90
            if quantity >= 5:
                # apply quantity discount
                price *= 0.95
            price = round(price,2)
            break
    except ValueError:
        print("Enter a number only please.")

print("Your final price is > $",format(price,'.2f'))

#TO DO - Proper testing
