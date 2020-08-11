#Exercise 77 - Year of Birth Calculator
# Question: Create a script that asks the user to enter their age and the script calculates the user's year of birth and prints it out in a string like 
# in the expected output. Please make sure you generate the current year dynamically.

import datetime

from datetime import *

age = int(input('Enter your age: '))
print(age)

#print(datetime.date.year())

print(date.today()) # O/P: 2020-08-09

print(datetime.today()) # O/P: 2020-08-10 19:11:50.824010
year = datetime.now().year  
print(year) # O/P: 2020

dob = year-age
print(dob) 


















