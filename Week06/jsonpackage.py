import json
#json takes double quotes, python takes double and single quotes
data = {
  'name':'joe',
  'age': 21,
  "student": True
  }

# print(data)
#create the file to hold the json 
file = open ("simple.json", 'w')
# transfer json to the file, intend 4 byte spaces for readibility
json.dump(data, file, indent=4)

#get a string for example to pass it up to a server
jsonString = json.dumps(data)

#note that it prints with double quotes as it is now a json object
print(jsonString)