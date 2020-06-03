# Make a script that prints out letters of English aplhabet from a to z. 

print(ord('a')) # Prints the unicode integer of char a.
# O/P: 97

print(chr(97)) # Represent unicode string of char a
# O/P: a

test = ['a']
uni_chr = int(97)

print(chr(uni_chr)) #O/P: a

for i in test:
    print(i) # O/P: a
    print(type(i)) # str

    #uni_chr = 98
    #print(chr(uni_chr)) # O/P: b
    #test.append(chr(uni_chr))
    #print(test)
    #uni_chr += 1
    
#print(test)


###################  SOLUTION ##############

import string

test = []

for letter in string.ascii_lowercase:
    test.append(letter)

print(test)

# O/P: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




