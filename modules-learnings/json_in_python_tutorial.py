'''

import json 

dump() and load()

serialization: encoding data into JSON format (More like writing to a file) = dump
Ex: Converting Python list to JSON 

De-serialization: decoding JSON data            (More like reading  a file) = load 
Ex: Reading JSON data into a Python list 

Serializaing JSON:

dump() - Write data to a file like object // List to JSON file

dumps() - Serialize our data into a string in JSON format. 


'''

import json

data = {
    "user":
    {
        "name": "William Williams",
        "age": 93
    }
}

with open('data_py.json', 'w') as input_file:
    json.dump(data, input_file, indent=4)

## To write the data as a string in memory use dumps()

json_str = json.dumps(data, indent=4)
print(json_str)

# O/P: {"user": {"name": "William Williams", "age": 93}}