import math
import Module1 as m1

worldRecords = {
	# AGE RANGE , MALE and FEMALE RECORDS IN SECONDS
    "<30" : [771,846],
	"30-39" : [774,873], 
    "40-49" : [786,904], 
    "50-59" : [893,1011], 
    "60-69" : [956,1079], 
    "70-79" : [1095,1256], 
    ">80" : [1258,1540]
}

def getDictKey( athAge ):
    # Returns the key for the world record dictionary
    # based on the variable athAge
    if int(athAge) < 30:
        return "<30"
    elif int(athAge) < 40:
        return "30-39"
    elif int(athAge) < 50:
        return "40-49"
    elif int(athAge) < 60:
        return "50-59"
    elif int(athAge) < 70:
        return "60-69"
    elif int(athAge) < 80:
        return "70-79"
    elif int(athAge) >= 80:
        return ">80"
    else:
        return "Invalid input"

def getAgeGraded( athAge, athGender, athTime ):
    # Check what format the athTime is in and change to seconds for calculations
    if isinstance(athTime,str):
        timeInSeconds = m1.convertTime( athTime, 'sec' )
    else:
        timeInSeconds = athTime
    # Get the key for the WR dictionary according to athAge
    dictKey = getDictKey( athAge )
    # Store the list of records in wrs
    wrs = worldRecords.get(dictKey,"Invalid key")
    
    if athGender.lower() == 'm':
        athRecord = wrs[0]
    elif athGender.lower() == 'f':
        athRecord = wrs[1]
    else:
        print("athGender is in the incorrect format.")

    ageGradedScore = str(round((athRecord/timeInSeconds)*100,2)) + " %"
    # print( "Inputs were",athAge,athGender,athTime )
    # print( "Result is: ",ageGraded,"%")
    return ageGradedScore

# TEST CASES
print("Test 1:",getAgeGraded( 33, 'm', "19:00"))
print("Test 2:",getAgeGraded( '33', 'm', "19:00"))
print("Test 3:",getAgeGraded( 33, 'm', 1140))
print("Test 4:",getAgeGraded( 33, 'm', 774))
print("Test 5:",getAgeGraded( 33, 'f', 774))



