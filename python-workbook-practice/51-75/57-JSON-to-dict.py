#Exercise 57 - JSON to Dictionary

# Question: use Python to print out the content of test_dump.json content.

#Expected output: 

#{'employees': [{'firstName': 'John', 'lastName': 'Doe'},
#               {'firstName': 'Anna', 'lastName': 'Smith'},
#               {'firstName': 'Peter', 'lastName': 'Jones'}],
# 'owners': [{'firstName': 'Jack', 'lastName': 'Petter'},
#            {'firstName': 'Jessy', 'lastName': 'Petter'}]}

import json

#with open('test_dump.json', 'r+') as file_to_read:
#    file_to_read.read('test_dump.json')
#    print(file_to_read.read('test_dump.json'))

## The above open command fails with this error - TypeError: argument should be integer or None, not 'str'

with open('test_dump.json', 'r+') as file_to_read:
    data = json.load(file_to_read)
    print(data)

# O/P: {'employees': [{'firstName': 'John', 'lastName': 'Doe'}, {'firstName': 'Anna', 'lastName': 'Smith'}, {'firstName': 'Peter', 'lastName': 'Jones'}], 'owners': [{'firstName': 'Jack', 'lastName': 'Petter'}, {'firstName': 'Jessy', 'lastName': 'Petter'}]}

#### ALTERNATIVE SOLUTION ##########

import json
from pprint import pprint
 
with open("test_dump.json","r") as file:
    d = json.loads(file.read())
 
pprint(d)

# O/P: {'employees': [{'firstName': 'John', 'lastName': 'Doe'},
             {'firstName': 'Anna', 'lastName': 'Smith'},
               {'firstName': 'Peter', 'lastName': 'Jones'}],
 'owners': [{'firstName': 'Jack', 'lastName': 'Petter'},
            {'firstName': 'Jessy', 'lastName': 'Petter'}]}




