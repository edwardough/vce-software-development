def myTerribleHash( uStr ):
    result = 0
    for char in uStr:
        result += ord( char )
    return result

while True:
    uInput = input("What you wanna hash? [Q] quit >> ")
    if uInput != 'Q':
        print(myTerribleHash( uInput ))
    else:
        break

input("[ENTER] to end.")
