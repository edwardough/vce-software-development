import json, time
from re import L

# stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
# pythonValue = { 'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None }

# airportFile = open('IATA_Airports.json')
with open('IATA_Airports.json') as airportFile:
    airportData = airportFile.read() # don't use readlines() with JSON
    print(f"File opened. Contains {len(airportData)} characters.")
    convertedJson = json.loads(airportData) #loads is short for 'load string'

countries = {}
for item in convertedJson:
    if item['country_code'] in countries.keys():
        countries[item['country_code']] += 1
    else:
        countries.update({item['country_code']:1})

countriesSorted = sorted(countries.items(), key=lambda i: i[1], reverse=True)
for country in countriesSorted:
    print('Country code:',country[0],'Num airports:',country[1])

while True:
    countryChoice = input('Which country would you like to view >> ')
    if countryChoice in countries.keys():
        break
    else:
        print("Invalid country code. Try again")

airports = []
for item in convertedJson:
    if item['country_code'] == countryChoice:
        airports.append({ 
                            'name' : item['name_translations']['en'],
                            'code' : item['code'],
                            'lat': item['coordinates']['lat'],
                            'lon': item['coordinates']['lon']
                        })
        # print(item['name_translations']['en'])

print("Total airports with matching country_code >> ", len(airports))
print("Information captured. Preparing to sort.")
choice = input("Enter sort [code] [name] [lat] [lon] or '' >> ")
if choice == '':
    choice = 'code'
airportsSorted = sorted(airports, key=lambda i: i[choice]) 
# sorted is a built in function that allows for a key
print("Information sorted. Preparing to print.")

for item in airportsSorted:
    print(item['code'], item['name'], item['lat'], item['lon'])
    time.sleep(0.10)

print("Exporting filtered results to JSON")

with open(countryChoice+'airportData.json', 'w') as exportFile:
    exportJson = json.dumps(airportsSorted)
    exportFile.write(exportJson)


