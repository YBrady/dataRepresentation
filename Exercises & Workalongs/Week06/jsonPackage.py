import json

# Python you can use singel or double quotes
data = {
    'name': 'Joe',
    'age': 21,
    "student": True
}

# Python will always print out singel quotes
print(data)

# JSON file will always have double quotes in it 
# (Either can be use din line below because it is Python)
file = open("simple.json","w")

# Putting an indent makes it look pretty in printout - easier to read but not required.
json.dump(data,file, indent = 4)

# This formats it to JSON
jsonString = json.dumps(data)
print(jsonString)