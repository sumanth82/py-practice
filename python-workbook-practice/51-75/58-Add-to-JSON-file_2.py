import json

with open('test_dump.json', 'r+') as file:
    d = json.loads(file.read())
    print(d)

    # O/P: 

    #{'employees': [{'firstName': 'John', 'lastName': 'Doe'},
    #           {'firstName': 'Anna', 'lastName': 'Smith'},
    #           {'firstName': 'Peter', 'lastName': 'Jones'}],
    #           'owners': [{'firstName': 'Jack', 'lastName': 'Petter'},
    #        {'firstName': 'Jessy', 'lastName': 'Petter'}]}

    d["employees"].append(dict(firstName ='Albert', lastName = 'Deeds'))
    print(d)
    file.seek(0)            # PUTS the CURSOR TO THE TOP OF THE FILE 
    # O/P: {'employees': [{'firstName': 'John', 'lastName': 'Doe'}, {'firstName': 'Anna', 'lastName': 'Smith'}, {'firstName': 'Peter', 'lastName': 'Jones'}, {'firstName': 'Albert', 'lastName': 'Deed'}], 'owners': [{'firstName': 'Jack', 'lastName': 'Petter'}, {'firstName': 'Jessy', 'lastName': 'Petter'}]}
    json.dump(d, file, indent=4, sort_keys=True)
    file.truncate()         # DELETES everything after the CURSOR;

    

