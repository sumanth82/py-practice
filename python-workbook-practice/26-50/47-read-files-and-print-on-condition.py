import sys
import os
import glob

empty_list = []

letters_folder = glob.glob('letters/*.txt')
print(type(letters_folder)) # List 
print(letters_folder)  

# O/P: ['letters/j.txt', 'letters/k.txt', 'letters/i.txt', 'letters/h.txt', 'letters/l.txt', 'letters/z.txt', 'letters/m.txt', 'letters/o.txt', 'letters/x.txt', 'letters/y.txt', 'letters/n.txt', 'letters/c.txt', 'letters/t.txt', 'letters/u.txt', 'letters/b.txt', 'letters/w.txt', 'letters/v.txt', 'letters/a.txt', 'letters/r.txt', 'letters/e.txt', 'letters/d.txt', 'letters/s.txt', 'letters/q.txt', 'letters/f.txt', 'letters/g.txt', 'letters/p.txt']

python_strings = [ 'p', 'y', 't', 'h', 'o', 'n']

for file in letters_folder:
        if (file == 'letters/p.txt') or (file == 'letters/y.txt') or (file == 'letters/t.txt') or (file == 'letters/h.txt' or (file == 'letters/o.txt') or (file == 'letters/n.txt')):
            required_python_strings = str(file)
            print(required_python_strings.split('/'))   # letters, p.txt
            print(list(required_python_strings.split('/'))) # ['letters', 'p.txt']
            list_of_required_python_strings = (list(required_python_strings.split('/')))
            print(list_of_required_python_strings)
            print(list_of_required_python_strings[1]) # p.txt
            print(type(list_of_required_python_strings[1])) # str
            print(list_of_required_python_strings[1].split('.')) # ['p', 'txt']
            print(type(list_of_required_python_strings[1].split('.'))) # list
            print(list_of_required_python_strings[1].split('.')[0]) # p 
            empty_list.append((list_of_required_python_strings[1].split('.')[0]))
            print(empty_list) # ['h', 'o', 'y', 'n', 't', 'p']
            