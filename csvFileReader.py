import csv

exampleFile = open('example.csv')
# read the file contents and store them in exampleReader
exampleReader = csv.reader(exampleFile)
# convert the file into a list format
exampleData = list(exampleReader)

print("Welcome to the csv reverser :)")

reversedList = []
for rows in exampleData:
    temp = []
    # range( start, end, step )
    for i in range(len(rows)-1,-1,-1):
        temp.append(rows[i])
    reversedList.append(temp)

outputFile = open('output.csv','w',newline='')
outputWriter = csv.writer(outputFile)

for row in reversedList:
    outputWriter.writerow(row)

outputFile.close()

