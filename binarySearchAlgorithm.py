import math

# Create a list of integers
def getListIntegers( length ):
	result = [1, 1]
	for i in range(length):
        # add the last two numbers in the results list together
		temp = result[-2] + result[-1]
		result.append( temp )
	return result

def binarySearch( arrayList, searchItem ):
    found = False
    listLen = len( arrayList )
    midPoint = math.floor( listLen / 2 )
    if arrayList[ midPoint ] == searchItem:
        found = True
    elif listLen > 1:
        if searchItem < arrayList[ midPoint ]:
            # Note the new search field will NOT include midpoint
            found = binarySearch( arrayList[0:midPoint], searchItem )
        else:
            # Note the new search field WILL include midpoint
            found = binarySearch( arrayList[midPoint:], searchItem)
    return found

print("Welcome to my BST thing")
searchList = getListIntegers(int(input("How many fibonacci numbers do you want? > ")))
print(searchList)
target = int(input("What number are you looking for? > "))
print(binarySearch(searchList, target))
print("Thanks to the BST algorithm that was super fast!")

