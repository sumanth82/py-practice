# Question: Please download the words1.txt file from the attachment and then create a Python function that takes a text file as input
# and returns the number of words contained in the text file.
#Expected output:
#10 

#def word_input():
#    open(word1.txt, r)

#print(word_input())

import os
import io
import pathlib

input_text = open('word1.txt', mode='r+')
print(input_text)
print(input_text.read())

# O/P: A tree is a woody perennial plant, typically with branches.

with open('word1.txt', mode='r+') as D:
    input_string = D.read()
    D = input_string.split(" ")
    print(D)

# O/P: ['A', 'tree', 'is', 'a', 'woody', 'perennial', 'plant,', 'typically', 'with', 'branches']

    print(len(D))

# O/P: 10



    #print(D.read().split('', maxsplit: -1))
    #input_value = D.read()
    #print(input_value)

# O/P: <_io.TextIOWrapper name='word1.txt' mode='r' encoding='UTF-8'>

# print(input_text.split())


#print(len(input_text.read()))

# O/P: 0

#print(type(input_text.read()))

# O/P: str

##### Example using pathlib module 

#p = Path('word1.txt')

#D = p.read_text()
#print(D)
