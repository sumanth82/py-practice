# In addition to previous problem, here a list of users already exist in a file called 'users.txt'
# Program should ask for a username and password. If the username already exists as in the 'users.txt' it should throw a message that the user already exists

username = input('Enter a username: ')

a=[]

with open('users.txt', 'r', newline='\n') as userfile:
    b= (userfile.readlines())
    print(b)    # O/P: ['Mercury\n', 'Venus\n', 'Earth\n', 'Mars\n', 'Jupiter\n', 'Saturn\n', 'Uranus\n', 'Neptune\n', 'Pluto\n', 'Neptune']
    print(type(b)) # list 

    #a = (userfile.read())
    #print(a)
    # O/P: Mercury
    #Venus
    #Earth
    #Mars
    #Jupiter
    #Saturn
    #Uranus
    #Neptune
    #Pluto
    #Neptune
    
    #print(type(a))  # str

    #input_list = list(a)
    #print(input_list)

# O/P: ['M', 'e', 'r', 'c', 'u', 'r', 'y', '\n', 'V', 'e', 'n', 'u', 's', '\n', 'E', 'a', 'r', 't', 'h', '\n', 'M', 'a', 'r', 's', '\n', 'J', 'u', 'p', 'i', 't', 'e', 'r', '\n', 'S', 'a', 't', 'u', 'r', 'n', '\n', 'U', 'r', 'a', 'n', 'u', 's', '\n', 'N', 'e', 'p', 't', 'u', 'n', 'e', '\n', 'P', 'l', 'u', 't', 'o', '\n', 'N', 'e', 'p', 't', 'u', 'n', 'e']


#    b= (userfile.readlines())
#    print(b)    # O/P: Empty List - []
#    print(type(b)) # list 


    for i in b:
        if i == username+'\n':
          print('Username already exists')
          break
    
    # O/P: If user inputs the password as 'Pluto', output is as expected - Username already exists
    ### WORKS GREAT :-) 




