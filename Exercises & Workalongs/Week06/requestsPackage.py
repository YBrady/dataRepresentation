import requests

# connecting to external website:
#url = 'https://www.gmit.ie'

#response = requests.get(url)

#print(response.status_code)
#print(response.text)
#print(response.headers)

# Posting to a website (using our own as an example)
url = 'http://127.0.0.1:5000/cars'
data = {'reg':'23h4', 'make': 'bljfls', 'model': 'hjfahk', 'price': 217}

# json = data makes sure site knows it is a JSON request
response = requests.post(url, json=data)

print(response.status_code)
print(response.json())