# Create a program that generates a password of 6 random alphanumeric characters in the range: abc....ABC...0123...!@#...

import random

print(random.random())  # O/P: 0.424200674396761 - All Floating

#print(random.SystemRandom())

chosen_password = random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*', 6)

print(chosen_password)

# Format - random.sample(population, k)
# population = set or sequenced
# k = length of the random letter

# O/P: ['K', 'P', '*', 'G', '^', '0']

required_output="".join(chosen_password)

print(required_output)# O/P: tgU$bK
print(random.shuffle(['a', 'b', 'c']))  # O/P: None


