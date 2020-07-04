# Exercise 63 - Progressive Time Printer with Threshold

#Question: Create a program that once executed the programs prints Hello  instantly first, then it prints it after 1 second, then after 2, 3, and 
# then the program prints out the message "End of the Loop" and stops.

#Expected output: 

#Hello
#Hello
#Hello
#Hello
#End of Loop

import time

i = 5

for index in range(i):
    if index < (i-1):
        print('Hello')
        time.sleep(index)
    else:
        print('End of Loop')


#O/P:
# Hello
#Hello
#Hello
#Hello
#End of Loop
#     

##### ALTERNATIVE SOLUTION #####

i = 0

while True:
    print('Hello')
    i = i + 1
    if i > 3:
        print('End of Loop')
        break
    time.sleep(i)

