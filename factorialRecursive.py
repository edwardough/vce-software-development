def factoRecursive( num ):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factoRecursive( num - 1 )
    # Using the function in it's own definition

def factoIterative( num ):
    result = 1
    for i in range(1, num + 1): # Using a for loop
        result = result * i
    return result

uNum = int(input("What number? " ))
print("Recursively:",factoRecursive(uNum))
print("Iteratively:",factoIterative(uNum))
