#Question: Count the number of "a" characters in this text file: http://www.pythonhow.com/data/universe.txt
#Expected output: 
#47

import requests

#print(dir(requests))

r = requests.get('http://www.pythonhow.com/data/universe.txt', headers = {'user-agent': 'customUserAgent'})
print(r.text)

got_text = r.text

print(type(r.text)) # str
empty_list = list(r.text)

counter=0

for i in range(len(empty_list)):
    if empty_list[i] == 'a':
        counter = counter +1
    else:
        pass

print(counter)

# O/P: 47

########## ALTERNATIVE SOLUTION ########


count_a = got_text.count("a")
print(count_a)















