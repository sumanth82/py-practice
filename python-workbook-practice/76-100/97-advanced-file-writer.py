# Enter a name, word, object as an input and it should be written to a file and saved only when user types SAVE. 
# 
# When user enters CLOSE, the program should save the previous entries and close.

list_a=[]

while True:
    name=input('Enter a name: ')
    with open('advanced-file-write.txt', 'a+') as file:
        list_a.append(name)
        if name == 'CLOSE':
            for i in list_a[:-1]:
                file.write(i+'\n')
            exit()
        else:
            if name == 'SAVE':
                for i in list_a[:-1]:
                    file.write(i+'\n')
                exit()

#### WORKS GREAT #####


