#Question: Store the dictionary in a json file.

#d = {"employees":[{"firstName": "John", "lastName": "Doe"},
#                {"firstName": "Anna", "lastName": "Smith"},
#                {"firstName": "Peter", "lastName": "Jones"}],
#"owners":[{"firstName": "Jack", "lastName": "Petter"},
#          {"firstName": "Jessy", "lastName": "Petter"}]}

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

print(type(d)) # <class 'dict'>

#with open('test.json', 'w+') as files:
#    files.write(d)

## This above with command - errors out as follows: TypeError: write() argument must be str, not dict

e = str(d)
print(type(e)) # <class 'str'>

with open('test.json', 'w+') as files:
    files.write(e + '\t')


####### 


import json 
import pprint

pprint.pprint(json.dumps(d))

# O/P: ('{"employees": [{"firstName": "John", "lastName": "Doe"}, {"firstName": '
 #'"Anna", "lastName": "Smith"}, {"firstName": "Peter", "lastName": "Jones"}], '
 #'"owners": [{"firstName": "Jack", "lastName": "Petter"}, {"firstName": '
 #'"Jessy", "lastName": "Petter"}]}')
with open('test-dumps.json', 'w+') as files_to_json:
      files_to_json.write(json.dumps(d))


###### ALTERNATIVE SOLN #####

with open('test_dump.json', 'w') as file_to_json:
    json.dump(d, file_to_json, indent=4)



