# Question:  Please write a function that calculates liquid volume in a sphere using the following formula. 
# The radius r  is always 10, so consider making it a default parameter.

#You can then test your solution by passing 2 for h and you should get the expected output.
#Expected output:
#4071.5040790523717

import math

x = math.pi
print(x) # O/P: 3.141592653589793

def test_func(h):

    r = 10
    lv = ((4*x*pow(r, 3))/3) - (((x*pow(h, 2)*((3*r)-h)))/3)
    return lv

print(test_func(2))

# O/P: 4071.5040790523717