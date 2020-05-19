#Question: Complete the script so that it produces the expected output. Please use my_range  as input data.

my_range = range(1, 21)

#Expected output: 
#[10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200] 

# SOLN:

my_range=range(1,21)
empty_list = []

print(my_range)
print(list(my_range))

for i in my_range:
    empty_list.append(i*10)
    
print(empty_list)

# O/P: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]












