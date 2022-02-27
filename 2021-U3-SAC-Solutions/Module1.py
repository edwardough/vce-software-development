import math

def convertTime( athTime, targetFormat ):
    if targetFormat == "mm:ss":
        # This means the time variable is in seconds
        minutes = math.floor( athTime / 60 )
        if minutes == 0:
            minutes = "00"
        elif minutes < 10:
            minutes = "0" + str(minutes)
        seconds = athTime % 60
        if seconds == 0:
            seconds = "00"
        elif seconds < 10:
            seconds = "0" + str(seconds)
        # use the str function in case they are still integers
        return str(minutes) + ":" + str(seconds) 
    elif targetFormat == 'sec':
        # This means the time variable is in mm:ss
        result = list(athTime.split(sep=":"))
        return int(result[0])*60 + int(result[1])
    else:
        print("Invalid format")

# TESTING COMPLETED

# athTime = convertTime( "18:45", "sec")
# print(athTime)
# athTime = convertTime( "00:45", "sec")
# print(athTime)
# athTime = convertTime( "00:00", "sec")
# print(athTime)
# athTime = convertTime( 690, 'mm:ss')
# print(athTime)
# athTime = convertTime( 590, 'mm:ss')
# print(athTime)
