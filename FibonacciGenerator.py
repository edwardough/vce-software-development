# a function for you to produce a 'special' list of sorted integers

def getListIntegers( length ):
	result = [1, 1]
	for i in range(length):
		temp = result[-2] + result[-1]
		result.append( temp )
	return result

getLength = int(input("How many sorted integers would you like? "))    
myList = getListIntegers( getLength )

print(myList)
