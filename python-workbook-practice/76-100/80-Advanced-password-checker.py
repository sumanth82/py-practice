# Create a script that lets the user submit a password until they have satisfied three conditions:

#1. Password contains atleast one number
#2. Contains one uppercase letter 
#3. It is atleast 5 characters long 

# Print the appropriate message for each of the reason of failure


input_password = input('Enter a password: ')


if any(i.isdigit() for i in input_password) and any(i.isupper() for i in input_password) and len(input_password)>=5:
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


########### ALTERNATIVE SOLUTION ###########

while True:
    notes = []
    if not any(i.isdigit() for i in input_password):
        notes.append('You need atleast 1 DIGIT')
    if not any(i.isupper() for i in input_password):
        notes.append('you need to have atleast 1 UPPERCASE letter')
    if len(input_password)<5:
        notes.append('the length should be greater than 5')
    if len(notes) == 0:
        print('password is fine')
        break
    else:
        print('Please check the following: ')
        for note in notes:
            print(note)
            break
    
        
    




    