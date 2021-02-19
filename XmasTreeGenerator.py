# imports
import math

# functions
def printTree( myTree ):
    for i in range(len(myTree)):
        for j in range(len(myTree[i])):
            print(myTree[i][j], end="")
        print("")

def initialiseTree( myHeight ):
    if myHeight % 2 == 1:
        result = []
        for i in range( myHeight ):
            temp = []
            for j in range( myHeight ):
                temp.append(' ')
            result.append(temp)
        return result
    else:
        result = []
        for i in range( myHeight ):
            temp = []
            for j in range( myHeight + 1 ):
                temp.append(' ')
            result.append(temp)
        return result

treeHeight = int(input("Enter tree height: "))
while treeHeight <= 0:
    print("Must be larger than 0")
    treeHeight = int(input("Enter tree height: "))

slashesState = False
totalChars = 1
treeTable = initialiseTree( treeHeight )
startSpot = math.floor( treeHeight / 2 )

for k in range(len(treeTable)):
    # for each row of the main tree
    for cr in range(totalChars):
        # this code block processes each row
        if cr == 0 and slashesState == True:
            # if slashesState = True and in first position place /
            treeTable[k][startSpot + cr] = "/"
        elif cr == totalChars - 1 and slashesState == True:
            # if slashesState = True and in last position place \
            treeTable[k][startSpot + cr] = "\\"
        else:
            # else normal fill character
            treeTable[k][startSpot + cr] = "*"
    if k % 2 == 0:
        # print("Finished processing row e{0,2,4,...}")
        startSpot -= 1
        totalChars += 2
        slashesState = True
    else:
        slashesState = False

printTree( treeTable )
