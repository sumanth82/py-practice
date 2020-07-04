#Exercise 62 - Progressive Timed Printer
#Question: Create a program that once executed the program prints Hello  instantly first, 
# then it prints it after 1 second, then after 2, 3, 4, and so on the interval increases between prints.
#Expected output: 

#...
#Hello
#Hello
#Hello
#Hello
#Hello
#Hello


import time

n = 1

while n>=1:
    print('Hello') 
    time.sleep(n)
    n+=1


#### ALTERNATIVE SOLN

i = 0
while True:
    i = i+1
    print('Hello')
    time.sleep(i)






