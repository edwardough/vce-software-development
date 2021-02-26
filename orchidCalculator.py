priceList = {
    'vandas' : 7.35,
    'miltonia' : 9.80,
    'cattleya' : 10.00
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
print("Member status:",member)
print("Chosen orchid:",orchid)
# TO DO Quantity input, finalPrice calculation
