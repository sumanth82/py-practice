# Create the fizz-buzz-item.py Script, Make It Executable with python3.7, and 
# Accept User Input
#Print "FizzBuzz" if the Value Is a Multiple of Three and Five
#Print "Fizz" if the Value Is a Multiple of Three, and "Buzz" if it's a Multiple of Five

i = int(input("Enter a number: "))

if (i % 3 == 0 and i % 5 == 0):
    print(f"FizzBuzz")
elif i % 3 == 0:
    print(f"Fizz")
elif i % 5 == 0:
    print(f"Buzz")
