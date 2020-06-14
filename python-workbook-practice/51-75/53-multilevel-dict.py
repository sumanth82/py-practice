#Question: Print out the last name of the second employee.

#Expected output: 
#Smith 

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

#for k, v in d.items():
#    print(k, ':')

# O/P: employees :
#owners :

#for employees in d.values():
#    print(employees)

for k,v in d.items():
    print(d['employees'])

    # O/P: 

    #[{'firstName': 'John', 'lastName': 'Doe'}, {'firstName': 'Anna', 'lastName': 'Smith'}, 
    # {'firstName': 'Peter', 'lastName': 'Jones'}]
    
    print(type(d['employees'])) # O/P: list
    
    x = d['employees']

    second_employee = x[1] 
    print(second_employee) # O/P: {'firstName': 'Anna', 'lastName': 'Smith'}
    print(second_employee['lastName']) # O/P: Smith

#########   ALTERNATIVE SOLUTION ##########

print(d['employees'][1]['lastName'])

# O/P: Smith