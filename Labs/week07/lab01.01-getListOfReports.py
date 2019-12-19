import requests
import json

# URL of API
#url = "https://reports.sem-o.com/api/v1/documents/static-reports"
url = "https://reports.sem-o.com/api/v1/documents/static-reports?ReportName=Balancing%20and%20Imbalance%20Market%20Cost%20View&Date=>2019-11-10"
response = requests.get(url)
# Load the data
data = response.json()

# Make an empty list for report list
listOfReports = []
#output to console
#print (data)

# Loop through each item
for item in data["items"]:
    #print(item["ResourceName"])
    # Add the ResourceName field to the list
    listOfReports.append(item["ResourceName"])

# Loop through each report
for ReportName in listOfReports:
    #print(ReportName)
    # Link to the report API
    url = "https://reports.sem-o.com/api/v1/documents/"+ReportName
    # Output to screen
    print(url)
    response = requests.get(url)
    # JSONify list
    aReport = response.json()

#other code
#save this to a file
filename = 'allreports.json'
# Writing JSON data
f = open(filename, 'w')
json.dump(data, f, indent=4)
