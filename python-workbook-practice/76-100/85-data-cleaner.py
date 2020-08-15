#Question: Please download the attached countries_raw.txt file. The file contains the list of country names, but it also contains some unnecessary text among the countries. 
#Please clean the list with Python by generating a new text file that contains a flawless list of country names without any other text or break lines in it. The new file content should look like in the expected output.

#Expected output: 

#Afghanistan
#Albania

with open('countries_raw.txt', 'r') as file:
    a=file.readlines()
    #print(a)

    #O/P: ['A\n', '\n', 'Afghanistan\n', 'Albania\n', 'Algeria\n', 'Andorra\n', 'Angola\n',........

with open('countries-raw.txt', 'w') as file:
    for line in a:
        if line.strip('\n')!="" and not line.isupper():
            file.write(line)

# O/P is as seen in file countries-raw.txt

