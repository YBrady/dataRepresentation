# import packages required
import requests
import json

# The apiKey for my repository
# Remove the minus from the key
apiKey = "1-7891d5635a02570115b7432abd1e11a6dab5790"
# The URL for the repository
url = "https://api.github.com/repos/YBrady/DataRepPrivate"

# Creating a file to save the content to
filename = "repo.json"

# Do the request
response = requests.get(url, auth=('token', apiKey))

# Jsonify it
repoJSON = response.json()
#print (response.json())

# Open and save it to the file
file = open(filename,"w")
json.dump(repoJSON,file, indent=4)