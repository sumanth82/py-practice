#Question: Create a program that prints out Hello  every two seconds.
#Expected output: 

#...
#Hello
#Hello
#Hello
#Hello
#Hello
#Hello

# https://realpython.com/python-sleep/
# import time and use time.sleep(<seconds>) method to sleep

import time

while True:
    print('Hello')
    time.sleep(5)
    
