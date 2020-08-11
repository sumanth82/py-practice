# Create a program that generates a password of 6 random alphanumeric characters in the range: abc....ABC...0123...!@#...

import random

print(random.random())  # O/P: 0.424200674396761 - All Floating

#print(random.SystemRandom())

print(random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*', 6))

# Format - random.sample(population, k)
# population = set or sequenced
# k = length of the random letter

# O/P: ['K', 'P', '*', 'G', '^', '0']

print(random.shuffle(['a', 'b', 'c']))  # O/P: None




