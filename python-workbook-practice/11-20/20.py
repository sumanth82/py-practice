# Question: Calculate the sum of all dictionary values.
# d = {"a": 1, "b": 2, "c": 3}
# Expected output: 
#6
# 

d = {"a": 1, "b": 2, "c": 3}
print(d["a"]+d["b"]+d["c"])

# O/P: 6

### ALTERNATIVE SOLN #####

x = d.values()   # use values() method to get all the values of a dict as a list
print(x)

# O/P: dict_values([1, 2, 3])

y = sum(x) # sum of all the values in the list 
print(y)

# O/P: 6









