# Import the required packages
import requests
import json

# Navigate to webpage from week 2 Lab
f = open("../week02/carviewer_Lab02.html", "r")
# Read the info from the page
html = f.read()
# Display the html source on screen
#print (html)

# Create an API key
apiKey = '60c7f40666bb5df3accd002e6092d68852133b3b026d79cb5fdb1fc12a310b48'
# Define the url to use for generation
url = 'https://api.html2pdf.app/v1/generate'

data = {'html': html,'apiKey': apiKey}
response = requests.post(url, json=data)

newFile = open("lab06.02.01.htmlaspdf.pdf","wb")
newFile.write(response.content)
print (response.status_code)