#import the required modules
import requests
import json

# The new car details
dataString = {'reg':'192 C 9523','make':'Lamborghini','model':'Urus','price':250000}
# The python webserver we created with the car daa
url = 'http://127.0.0.1:5000/cars'
# Send the request and write response back to response
response = requests.post(url, json=dataString)
# Display the response code (all going well should be 201)
print (response.status_code)