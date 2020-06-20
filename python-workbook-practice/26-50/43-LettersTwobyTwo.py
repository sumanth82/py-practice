# Question: Create a script that generates a file where all letters of English alphabet are listed two in each line. 
# The inside of the text file would look like:

#ab
#cd
#ef

#and so on.

import string

print(list(zip(string.ascii_lowercase, string.ascii_letters)))

# O/P: [('a', 'a'), ('b', 'b'), ('c', 'c'), ('d', 'd'), ('e', 'e'), ('f', 'f'), ('g', 'g'), ('h', 'h'), ('i', 'i'), ('j', 'j'), ('k', 'k'), ('l', 'l'), ('m', 'm'), ('n', 'n'), ('o', 'o'), ('p', 'p'), ('
# q', 'q'), ('r', 'r'), ('s', 's'), ('t', 't'), ('u', 'u'), ('v', 'v'), ('w', 'w'), ('x', 'x'), ('y', 'y'), ('z', 'z')]

test = (list(zip(string.ascii_lowercase[0:1], string.ascii_letters[1:2]))) # O/P: [('a', 'b')]

print(test)
print(str(test))

test1 = (list(zip(string.ascii_lowercase[0::2], string.ascii_letters[1::2]))) # O/P: [('a', 'b')]
print(test1) # O/P: [('a', 'b'), ('c', 'd'), ('e', 'f'), ('g', 'h'), ('i', 'j'), ('k', 'l'), ('m', 'n'), ('o', 'p'), ('q', 'r'), ('s', 't'), ('u', 'v'), ('w', 'x'), ('y', 'z')]


with open('separate_script.txt', 'w+') as files:
    for letter1, letter2 in zip(string.ascii_lowercase[0::2], string.ascii_letters[1::2]):
        files.write(letter1 + letter2 + '\n')





