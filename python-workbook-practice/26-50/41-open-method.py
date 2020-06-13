# Question: Create a script that generates a text file with all letters of English alphabet inside it, one letter per line.

import string

print(string.ascii_lowercase) # O/P: abcdefghijklmnopqrstuvwxyz

test = []
for letter in string.ascii_lowercase:
    test.append(letter)

print(test)

# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# In open() function below, 'file' is a variable.
# You can do a file.read() to read from the file test.txt or file.write() to write to the file variable


with open('test.txt', mode='w+', newline='\n') as file:
    file.write('Hello open()')

# Now if you open the test.txt file, you will see - Hello open() written to it;

with open('test.txt', 'r') as input:
    print(input.read()) # O/P: Hello open()

# To the original problem:    

with open('test_string.txt', mode='w+', newline='\n') as file:
    a = string.ascii_lowercase
    print(a)
    file.write(a) # Writes the above to a file 


#### This works #####

with open('test_string_new.txt', mode='w+', newline='\n') as file:
    for letters in string.ascii_lowercase:
        print(letters)
        file.write(letters)
        file.write("\n")

###     ALternate Solution  #####

with open("letters.txt", "w") as file:
    for letter in string.ascii_lowercase:
        file.write(letter + "\n")


        











