# Create the fizz-buzz.py Script, Make It Executable with python3.7, and 
# Accept User Input

# Create a Range from 1 to the User's Provided Number and Loop Through It
# Print "FizzBuzz" if the Value Is a Multiple of Three and Five
# Print "Fizz" if the Value Is a Multiple of Three and "Buzz" if It's a Multiple of Five

u = int(input("Enter a favorite number: "))
u+=1

for i in range(1, u):
    if (i % 3 == 0 and i % 5 == 0):
        print(f"FizzBuzz")
        break
    elif i % 5 == 0:
        print(f"Buzz")
        break
    elif i % 3 == 0:
        print(f"Fizz")
        break

