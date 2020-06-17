# Extract the letters in 26 files and put it and print out as a list;

import glob

letters = [ ]
data = glob.glob('./letters/*.txt')

for file_name in data:
    with open(file_name, 'r') as file:
        letters.append(file.read().strip('\n'))
    
print(sorted(letters))

# O/P: 

['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w'
, 'x', 'y', 'z']