# Create the split_names Function to Separate Names

# Create the is_palindrome Function to Determine if a String or Number Is a 
# Palindrome Ex: 'radar'

# Create the build_list Function to Take an Item and a Count and Return 
# a List with item Repeated count Times

def split_names(x):
    first_name, middle_name, last_name = x.split(maxsplit=2)

    return {
       print(f"'firstname': {first_name}"),
       print(f"'middlename': {middle_name}"),
       print(f"'lastname': {last_name}"),
    }

def is_palindrome(y):
    y = str(y)
    y == y[::-1] # This is the syntax to reverse a string or a number
    if y == y[::-1]: 
        print(f"This given item {y} is a palindrome")
    else:
        print(f"The given item {y} is not a palindrome")
    return y

def build_list(item, count=1):
    items = []
    for i in range(count):
        items.append(item)
    print(items)   # O/P: ['Apple', 'Apple', 'Apple', 'Apple', 'Apple']
    return items

split_names('Michael J Schumacher')
    
# O/P: 'firstname': Michael
#'middlename': J
#'lastname': Schumacher

is_palindrome("saas")

build_list("Apple", 5)

