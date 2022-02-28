import json, csv

with open('dunkinDonuts.json') as donutFile:
    donutData = donutFile.read() # don't use readlines() with JSON
    print(f"File opened. Contains {len(donutData)} characters.")
    convertedJson = json.loads(donutData) #loads is short for 'load string'

# Print a single record. We had to 'dive' into the json file to see 
# what we were dealing with here.
print(convertedJson['data'][0])
# TODO Investigate using pprint to print this out with indentation, readability enhanced.

targetData = [{
            'address':'address',
            'phone':'phonenumber',
            'recordID':'recordId' }]

for item in convertedJson['data']:
    if item['almond'] == 'Y':
        targetData.append({
            'address':item['address'],
            'phone':item['phonenumber'],
            'recordID': item['recordId']
        })

# for store in targetData:
#     print(store)

with open('dunkinDonuts.csv','w', newline="") as donutCsv:
    outputWriter = csv.writer(donutCsv) # don't use readlines() with JSON
    for row in targetData:
        outputWriter.writerow(row.values())

input('Enter to end')