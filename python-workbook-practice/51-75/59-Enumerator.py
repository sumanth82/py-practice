#Question: Please complete the code so that it prints out the expected output.
#a = [1, 2, 3] 
#Expected output: 

#Item 1 has index 0
#Item 2 has index 1
#Item 3 has index 2

a = [1, 2, 3]
#for i in enumerate(a):
#    print('Item', i, 'has index', enumerate[a])

print(list(enumerate(a)))

# [(0, 1), (1, 2), (2, 3)]

for i in list(enumerate(a)):
    print('Item', i, 'has index', list(enumerate(a)))

#Item (0, 1) has index [(0, 1), (1, 2), (2, 3)]
#Item (1, 2) has index [(0, 1), (1, 2), (2, 3)]
#Item (2, 3) has index [(0, 1), (1, 2), (2, 3)]


for index, items in enumerate(a):
    print('Index value', index, 'is what it is for items: ', items)


#Index value 0 is what it is for items:  1
#Index value 1 is what it is for items:  2
#Index value 2 is what it is for items:  3

# enumerate(a)  creates an enumerate object which yields pairs of indexes and items



