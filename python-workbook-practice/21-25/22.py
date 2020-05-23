# Create a dict that has 3 keys a,b,c and value - a list from 1 to 10, 11 to 20, 21 to 30

d = dict()

d['a'] = [1,2,3,4,5,6,7,8,9,10]
d['b'] = [11,12,13,14,15,16,17,18,19,20]
d['c'] = [21,22,23,24,25,26,27,28,29,30]

print(d) # O/P: {'a': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'b': [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 'c': [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]}


###### ALTERNATIVE SOLN #####

d = {'a': list(range(1,11)), 'b': list(range(11, 21)), 'c': list(range(21, 31))}

print(d) # O/P: {'a': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'b': [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 'c': [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]}








