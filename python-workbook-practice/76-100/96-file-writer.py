# Enter a name, word, object as an input and it should be written to a file. When user enters CLOSE, the program should close and exit.
# When the user starts the program again it should append the file with the new entries.
# 

while True:
    name = input('Enter a word: ')
    if name=='CLOSE':
        exit()
    else:
        with open('file-writer.py', 'a') as file:
            file.write(name+'\n')

### WORKS GREAT 

### ALTERNATIVE SOLUTION ###

input_file=open('user-data.txt', 'a+')

while True:
    line = input('Enter a name: ')
    if line == 'CLOSE':
        input_file.close()
        break
    else:
        file.write(line + '\n')




    

