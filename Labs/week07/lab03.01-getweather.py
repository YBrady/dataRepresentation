import requests
import json

# URL of api
url = "https://prodapi.metweb.ie/observations/cork/today"
# Gets the data
response = requests.get(url)
# Load the data into data 
data = response.json()

# Loop through each row
for row in data:
    # Print out humidity
    print(row["temperature"])


#save this to a file
#filename = 'weatherReports.json'
# Writing JSON data
#f = open(filename, 'w')
#json.dump(data, f, indent=4)
