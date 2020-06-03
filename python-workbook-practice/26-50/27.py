# Question: 

# Create a function that calculates acceleration given initial velocity v1, final velocity v2, start time t1, and end time t2. 
# The formula for acceleration is:

# a = v2-v1 / t2-t1

# To test your solution, call the function by inputting values 0, 10, 0, 20 for v1, v2, t1, and t2 respectively, and you should get the expected output.

#Expected output:
# 0.5

def test(num1,num2,num3,num4):
    a = num2-num1
    b = num3-num4
    
    z = a/b
    -z  // Negate value of z -(-0.5) = + 0.5
    print(-z)
    return -z

print(test(0,10,0,20))

# O/P: 0.5







