#Exercise 55 - Adding to Multilevel Dictionaries

#Question: Please add a new employee to the dictionary.

#d = {"employees":[{"firstName": "John", "lastName": "Doe"},
#                {"firstName": "Anna", "lastName": "Smith"},
#                {"firstName": "Peter", "lastName": "Jones"}],
#"owners":[{"firstName": "Jack", "lastName": "Petter"},
#          {"firstName": "Jessy", "lastName": "Petter"}]}

#Expected output: 

#{'employees': [{'firstName': 'John', 'lastName': 'Doe'},
##               {'firstName': 'Anna', 'lastName': 'Smith'},
#               {'firstName': 'Peter', 'lastName': 'Jones'},
#               {'firstName': 'Albert', 'lastName': 'Bert'}],
# 'owners': [{'firstName': 'Jack', 'lastName': 'Petter'},
#            {'firstName': 'Jessy', 'lastName': 'Petter'}]}

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

for v in d.values():
        if d['employees']:
    #print(d['employees'])  # [{'firstName': 'John', 'lastName': 'Doe'}, {'firstName': 'Anna', 'lastName': 'Smith'}, {'firstName': 'Peter', 'lastName': 'Jones'}]
            d['employees'].append(dict([('firstname','Sumant'), ('lastName', 'Renukarya')]))
            break
    
print(d)

# O/P: {'employees': [{'firstName': 'John', 'lastName': 'Doe'}, {'firstName': 'Anna', 'lastName': 'Smith'}, {'firstName': 'Peter', 'lastName': 'Jones'}, {'firstname': 'Sumant', 'lastName': 'Renukarya'}], 'owners': [{'firstName': 'Jack', 'lastName': 'Petter'}, {'firstName': 'Jessy', 'lastName': 'Petter'}]}

