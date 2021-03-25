import time, math, csv
import Module1 as m1

# Allows user to confirm event start
while True:
    temp = input("Type [START] to start the event > ")
    if temp == 'START':
        break

startTime = time.perf_counter()
timerStatus = True

# Create a list with a single time in it.
athleteLog = [0]

while timerStatus == True:
    addRecord = input("[Q] to quit, [ENTER] to record > ")
    if addRecord.upper() == 'Q':
        finalCheck = input("[Y] to confirm quit, ending the event > ")
        if finalCheck.upper() == 'Y':
            timerStatus = False
        else:
            print("Event continues")
    else:
        print("Adding time.")
        currTime = int(round(time.perf_counter(),0))
        temp = m1.convertTime( currTime, 'mm:ss')
        athleteLog.append(temp)

print("Event completed.")
print(athleteLog)

outputFile = open('results.csv','w',newline='')
outputWriter = csv.writer(outputFile)

for i in range(1,len(athleteLog)):
    place = "P" + str(i)
    temp = [place, athleteLog[i]]
    outputWriter.writerow(temp)

# close the file
outputFile.close()

print("--- results.csv created ---")


