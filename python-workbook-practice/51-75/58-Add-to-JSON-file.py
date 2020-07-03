#Question: Please download the json file in the attachment and use Python to add a new employee 
#to the content of the file so that the file looks like in the expected output below.
# Use test_dump.json as input


# Add new employee:

#           "firstName": "Albert",
#            "lastName": "Bert"

#Expected output: 

import json
import pprint

with open('test_dump.json', 'rb') as read_json:
    #data = json.load(read_json)
    data=json.loads(read_json.read())

pprint.pprint(data)

# O/P: {'employees': [{'firstName': 'John', 'lastName': 'Doe'},
#               {'firstName': 'Anna', 'lastName': 'Smith'},
#               {'firstName': 'Peter', 'lastName': 'Jones'}],
# 'owners': [{'firstName': 'Jack', 'lastName': 'Petter'},
#            {'firstName': 'Jessy', 'lastName': 'Petter'}]}

print(type(data))   # O/P: dict

#employees_list = data['employees']
#print(employees_list)

# O/P: [{'firstName': 'John', 'lastName': 'Doe'}, {'firstName': 'Anna', 'lastName': 'Smith'}, {'firstName': 'Peter', 'lastName': 'Jones'}]

#print(type(employees_list)) # O/P: List

#employees_list.append({'firstName': 'Albert', 'lastName': 'Deed'})
#print(employees_list)
# O/P: [{'firstName': 'John', 'lastName': 'Doe'}, {'firstName': 'Anna', 'lastName': 'Smith'}, {'firstName': 'Peter', 'lastName': 'Jones'}, {'firstName': 'Albert', 'lastName': 'Deed'}]


data['employees'].append(dict(firstName= 'Albert', lastName = 'Deed'))

print(data)

#data = data + data['employees'][0]['firstName'] = "Albert"
#data = data + data['employees'][0]['lastName'] = "Bert"

#pprint.pprint(data)

#data_new= {'employees': [{'firstName': 'Albert', 'lastName': 'Bert'}]}
#pprint.pprint(data_new)

#pprint.pprint(data.update(data_new))

#pprint.pprint(data)

#data1 = {"username": "Timon"}

#with open('test_dump.json', 'w+') as input_json:
#    json.dump(data, input_json)

# O/P: This writes the data to the test_dump.json file







