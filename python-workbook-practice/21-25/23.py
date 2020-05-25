# Question: Access the third value of key b  from the dictionary.
#from pprint import pprint
#d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))
#Expected output: 
#13  

d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))
print(d)

print(d['b']) # O/P: [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for i, v in enumerate(d['b']):
    if i == 2:
        print(v)
        break

# O/P: 13

### ALTERNATIVE SOLN ###

print(d['b'][2]) # O/P: 13














