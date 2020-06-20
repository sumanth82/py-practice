#Exercise 44 - Letters Three by Three
#Question: Create a script that generates a file where all letters of English alphabet are listed three in each line. The inside of the text file would look like:
#abc
#def
#ghi
#and so on.

import string

print(list(zip('a', 'b'))) # [('a', 'b')]

with open('three-by-three.txt', 'w+') as files:
    for letter1, letter2, letter3 in zip(string.ascii_letters[0::3], string.ascii_lowercase[1::3], string.ascii_lowercase[2::3]):
        files.write(letter1 + letter2 + letter3 + '\n')




