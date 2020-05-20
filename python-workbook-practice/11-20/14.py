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

