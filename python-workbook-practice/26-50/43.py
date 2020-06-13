# Question: Create a script that generates a file where all letters of English alphabet are listed two in each line. 
# The inside of the text file would look like:

#ab
#cd
#ef

#and so on.

import string

with open('separate_script.txt', 'w+') as files:
    
    for letter in string.ascii_lowercase:
        print(len(letter)) # O/P: 1
        print(letter)
        temp = letter 




