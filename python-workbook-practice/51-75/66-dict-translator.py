#Question: Create an English to Portuguese translation program.
#The program takes a word from the user as input and translates it using the following dictionary as a vocabulary source.
#d = dict(weather = "clima", earth = "terra", rain = "chuva") 

#Expected output: 
#Enter word: earth
#terra


input_word = input('Enter a word: ')
d = dict(weather = "clima", earth = "terra", rain = "chuva") 
print(d[input_word])









