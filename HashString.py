myList = list(input("Enter a string for hashing: "))
myKey = int(input("Enter a numeric password between 1 and 255: "))

# If the list is odd in length add a blank space
if len(myList) % 2 == 1:
    myList.append(" ")

# Create an empty list for the result
hashResult = []

# Loop through the list, grab each pair, operate on them, add the result to the list
# Note that i goes up by 2 but cannot be larger than length - 1
for i in range(0,len(myList)-1,2):
    # display the pairs - testing purposes
    print("Pair",int((i/2)+1),":",myList[i],myList[i+1])
    # (firstItem & key ) | secondItem
    # Note
    # "&" is boolean AND
    # "<<" shifts all the bits to the left
    # "|" is boolean OR
    # They are bit level operations
    # ord converts the character to it's numeric equivalent on the ASCII table (more info below)
    # http://sticksandstones.kstrom.com/appen.html
    temp = (ord(myList[i]) & myKey) | ( (ord(myList[i+1]) << 3) & 255 )
    hashResult.append(temp)

# When you want to turn a list into a string use join with a blank string    
print( "The numeric hash list is:", hashResult )

for num in hashResult:
    # chr() converts a number into it's character equivalent on the ASCII table
    # eg chr(65) would print 'A'
    print(chr(num),end="")

print("\nThanks for using HashString")

# TO DO
# The hash is only half the length of the input - for large inputs (eg "holyBible.txt") this is not a large enough reduction.
# So if the hashResult is of a certain length the process could be repeated until it is 8 characters long or something like that.
