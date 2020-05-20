# Question: Complete the script so it generates the expected output using my_range  as input data. 
# Please note that the items of the expected list output are all strings.

#my_range = range(1, 21)
# Expected output: 

#['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']  

my_range = range(1, 21)

print(my_range) # O/P: range(1, 21)
print(str(my_range)) # O/P: range(1, 21)

# Notes: str() function converts numbers to strings 
# map() is a built-in function used to convert list to strings

map(str, my_range) # Takes an empty str function and iterates using the range
print(map(str, my_range))

# O/P: <map object at 0x109222bd0>

print(list(map(str, my_range)))

# O/P: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']





