#Question: Please download the json file in the attachment and use Python to add a new employee 
#to the content of the file so that the file looks like in the expected output below.
# Use test_dump.json as input


# Add new employee:

#           "firstName": "Albert",
#            "lastName": "Bert"

#Expected output: 

import json 

with open('test_dump.json', 'r+') as input_json:
    print(input_json.read(json.loads(input_json)))








