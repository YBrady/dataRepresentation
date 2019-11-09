# Import the modules
import requests

# URL - python car server - with reg included with %20's
url = 'http://127.0.0.1:5000/cars/192%20C%209523'

# Do request and save response
response = requests.delete(url)

# Display response code (should be 200)
print (response.status_code)
# Display response text (should be "true")
print (response.text)