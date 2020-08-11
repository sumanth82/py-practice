# Create a script that lets the user submit a password until they have satisfied three conditions:

#1. Password contains atleast one number
#2. Contains one uppercase letter 
#3. It is atleast 5 characters long 

# Print message 'password is not fine' if the user didn't create a password.

input_password = input('Enter a password with the prescribed requirement: ' )

## Covert a String to a list:

split_password=list(input_password)
print(split_password)

# O/P: ['t', 'e', 's', 't']

counter=0

for i in split_password:
    if str.isdigit(i) or str.isupper(i) and len(split_password)>=5:
        print('All Good')
    else:
        print('Password is NOT fine')



#if (str.isdigit(input_password))=True and (str.isupper(input_password))=True and len(input_password) > 5:
#    print('Password is as expected')


#for i in split_password:
#    if i
#if not int or not uppercase() or not len(5):
#    print('Doesnt meet the requirements')
#else:
#    print(input_password)