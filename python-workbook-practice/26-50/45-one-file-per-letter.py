#Question: Please create a script that generates 26 text files named a.txt, b.txt, and so on up to z.txt. Each file should contain a letter reflecting its filename. So, a.txt will contain letter a, b.txt will contain letter b and so on.

import string

letters = string.ascii_lowercase
print(letters) # O/P: abcdefghijklmnopqrstuvwxyz
print(type(letters)) # O/P: str

print(list(letters)) # O/P: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

letters_in_list = list(letters)

## Below 2 lines create a file - a.txt and has the contenst of it as a

#with open('a.txt', 'w') as file:   
#    file.write('a')

for i in letters_in_list:
    i = i+'.txt'
    #print(i)
    with open(i, 'w+') as file:
        i = i.replace('.txt', ' ')
        #print(i)
        file.write(i)






