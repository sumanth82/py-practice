#Question: Create an English to Portuguese translation program.

#The program takes a word from the user as input and translates it using the following dictionary as a vocabulary source. In addition, return the message "We couldn't find that word!" when the user enters a word that is not in the dictionary. 

#Also, make the program non case-sensitive meaning that for example, both earth and Earth should return the translation correctly for that word.

#d = dict(weather = "clima", earth = "terra", rain = "chuva") 

#Expected output: 

#Enter word: hello
#We couldn't find that word!

input_word = input('Enter a word : ')

d = dict(weather = "clima", earth = "terra", rain = "chuva")

#print(d['weather'])

print(type(d['weather']))   # O/P: str

input_keys = list(d.keys())
print(input_keys)
print(type(input_keys)) # O/P: str

counter = 0

for i in range(len(input_keys)):
    
    if input_word.casefold() == input_keys[i]:
        print('The word is found')
        counter = counter + 1
        break
    else:
        if counter == i and input_word.casefold() != input_keys[i]:
            print("Word Not found")
        else:
            counter+=1
            pass



