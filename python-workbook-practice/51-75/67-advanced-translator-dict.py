#Question: Create an English to Portuguese translation program.

#The program takes a word from the user as input and translates it using the following dictionary as a vocabulary source. 
# In addition, try to return the message "We couldn't find that word!" when the user enters a word that is not in the dictionary.

#d = dict(weather = "clima", earth = "terra", rain = "chuva") 

#Expected output: 

#Enter word: hello
#That word doesn't exist!

input_word = input('Enter a word : ' )
d = dict(weather = "clima", earth = "terra", rain = "chuva")

list_of_values = (list(d.values()))
print(list(d.values()))
# O/P: []'clima', 'terra', 'chuva']

list_of_keys = (list(d.keys()))
print(list(d.keys()))

#O/P: ['weather', 'earth', 'rain']

for i in range(len(list_of_keys)):
    if list_of_keys[i] == input_word:
        print('The dict word for', input_word, 'is', list_of_values[i])
        break
    else:
        pass

print('That word doesn\'t exist')

#O/P:

#Enter a word : weather
#['clima', 'terra', 'chuva']
#['weather', 'earth', 'rain']
#The dict word for weather is clima
#That word doesn't exist

#### WORKING SOLUTION - Use try, except KeyError #####

def test_func(input_word):
    try:
        return d[input_word]

    except KeyError:
        return "The word does not exist"

print(test_func(input_word))


