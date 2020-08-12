# In addition to previous problem, here a list of users already exist in a file called 'users.txt'
# Program should ask for a username and password. If the username already exists as in the 'users.txt' it should throw a message that the user already exists

input_password = input('Enter a password: ')

## Step-1: If UserName already exists in the file - users.txt then print the message and fail the program

with open('users.txt', 'r', newline='\n') as userfile:
    b= (userfile.readlines())
    print(b)    # O/P: ['Mercury\n', 'Venus\n', 'Earth\n', 'Mars\n', 'Jupiter\n', 'Saturn\n', 'Uranus\n', 'Neptune\n', 'Pluto\n', 'Neptune']
    print(type(b)) # list 

    #for i in b:
    #    if i == input_password+'\n':
    #      print('Username already exists')
    #      break
    
    # O/P: If user inputs the password as 'Pluto', output is as expected - Username already exists
    ### WORKS GREAT :-) 

if any(i==input_password+'\n' for i in b):
    print('Username already exists')
    
    
    # O/P: If user inputs the password as 'Pluto', output is as expected - Username already exists
    ### WORKS GREAT :-) 

elif any(i.isdigit() for i in input_password) and any(i.isupper() for i in input_password) and len(input_password)>=5:
    print('Password is fine')
elif (any(i.isdigit() for i in input_password))!=True and (any(i.isupper() for i in input_password))!=True and len(input_password)>=5:
    print('You need atleast one DIGIT and one UPPERCASE')
elif any(i.isdigit() for i in input_password) and any(i.isupper() for i in input_password) and len(input_password)<5:
    print('You must have atleast 5 letters')
elif any(i.isupper() for i in input_password) and (any(i.isupper() for i in input_password))!=True and len(input_password)>=5:
    print('you must have atleast one UPPERCASE')
elif any(i.isdigit() for i in input_password) and (any(i.isupper() for i in input_password))!=True and len(input_password)<5:
    print('you must have atleast one UPPERCASE and 5 letters')
elif (any(i.isdigit() for i in input_password))!=True and any(i.isupper() for i in input_password) and len(input_password)<5:
    print('you must have atleast one DIGIT and 5 letters')
else:
    print('Man - Out of options')

### WORKS GREAT #####


