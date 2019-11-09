# Import the modules
import requests
import json

# The update details
dataString = {'make':'Tesla','model':'Model X'}
# The URL for our cars
url = 'http://127.0.0.1:5000/cars/test'
# Sending the request and writing the response back to response
response = requests.put(url, json=dataString)
# Display results - status code
print (response.status_code)
# Full results
print (response.text)