#Question: Print out in each line the sum of homologous items of the two sequences.

#a = [1, 2, 3]
#b = (4, 5, 6)

#Expected output: 

#5
#7
#9

a = [1, 2, 3] # This is a list
b = (4, 5, 6) # This is a tuple 

x = a[0]+b[0]
print(x)

y = a[1] + b[1]
print(y)

z= a[2]+b[2]
print(z)

##### ALTERNATIVE SOLUTION -- Use zip() ######

# Use zip () to bind vars of two different types and iterate over each var, element by element. 

print(zip(a,b))
print(list(zip(a, b)))

# O/P: [(1, 4), (2, 5), (3, 6)]

for i, j in zip(a, b):
    print(i + j)

# 5
#7
#9




