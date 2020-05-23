# Question: Filter the dictionary by removing all items with a value of greater than 1.
#d = {"a": 1, "b": 2, "c": 3}
#Expected output: 
#{'a': 1}  

d = {"a": 1, "b": 2, "c": 3}

### a. Retrieve the values using values() method for a dict. ####

d1 = d.values()
print(d1)        # O/P: dict_values([1, 2, 3])

d2 = list(d1)    
print(d2)       # O/P: [1, 2, 3]

#for i in d2:
#    if d2[i] > 1:
#        del d2[i]
#    print(d2)

### b. Retrieve the keys using list(d) for a dict ###

d3=list(d)
print(d3)     # O/P: ['a', 'b', 'c']

### c. For sorting the keys, used sorted(d) ###

d4 = sorted(d)
print(d4)   # O/P: ['a', 'b', 'c']

### d. 

for k, v in d.items():
    print(d.items()) # O/P: dict_items([('a', 1), ('b', 2), ('c', 3)])
    print(list(d.items())) # O/P: [('a', 1), ('b', 2), ('c', 3)]
    x = list(d.items())
    print(x)

for i in d.values():
    print(d.values())
    #if d.values() > 1:
    #    del d

#### SOLN - Use dict() comprehension i.e expression within dict()

d = dict((k, v) for k, v in d.items() if v <= 1 )
print(d)  # O/P : {'a': 1}










    
