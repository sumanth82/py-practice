#Question: Complete the script so that it removes duplicate items from list a .
#a = ["1", 1, "1", 2]
#Expected output: 
#  ['1', 2, 1] 

a = ["1", 1, "1", 2]

print(a)    # O/P: ['1', 1, '1', 2]
print(type(a))   # O/P: <class 'list'>

b = set()   # Create an empty set()

print(type(b)) # O/P: <class 'set'>

def test_set(x):
    for i in x:
        b = x
        return b

test_set(a)

print(test_set(a)) # O/P: ['1', 1, '1', 2]
print(type(test_set(a))) # O/P: <class 'list'>

print(set(test_set(a))) # O/P: {1, 2, '1'}
print(list(set(test_set(a)))) # O/P: ['1', 2, 1]


# LEARNING: Set is an unordered collection with NO duplicate elements 
# Define a empty set as - set() or set = {'x', 'x', 'y'}



######################### ALTERNATIVE SOLNS ###############################

Answer 2:

from collections import OrderedDict
a = ["1", 1, "1", 2]
a = list(OrderedDict.fromkeys(a))
print(a)
Explanation 2:

Ordered dictionaries are another data type in Python that unlike sets and normal dictionaries they preserve the order of the items. 
Here OrderedDict.fromkeys(a)  would produce an OrderedDict  like [('1', None), (1, None), (2, None)] . Then we would convert that OrderedDict  to a list.

Answer 3:

a = ["1", 1, "1", 2]
b = []
for i in a:
    if i not in b:
        b.append(i)
Explanation 3:

This is another solution that would preserve the original order. We go through all items of the original list and 
append them to the new list if they have not been appended before. The downside of this is the operation can take a lot of time if the list is large 
as we need to access both lists and also perform a conditional in each iteration.