import sys
import os
import glob


empty_list = []

letters_folder = glob.glob('letters/*.txt')
print(type(letters_folder)) # List 
print(letters_folder)

for file in letters_folder:
    if file == 'letters/p.txt':
        got_output = str(file)
        print(got_output)   # letters/p.txt
        print(type(got_output)) # <class 'str'>



#for file in letters_folder:
#    if file == any_string_of_python
#    empty_list = empty_list.append(file)
#    print(empty_list) 


