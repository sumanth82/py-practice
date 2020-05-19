# Create the char_range Generator
# Include the Stop Character in the Results
# Support the Start Code Point Being More Than the Stop Code Point

def char_range(start, stop, step=1):
    start_code = ord(start) # ord() - Returns the int value representing the Unicode code point of char. 
    stop_code = ord(stop) # 
    stop_modifier = 1
    print(start_code)
    print(stop_code)
    if start_code > stop_code:
        step *= -1
        stop_modifier *= -1
    for value in range(start_code, stop_code + stop_modifier, step):
        yield chr(value)   # chr(i) - Turn int i into str 
    
char_range('a', 'z', '1')

