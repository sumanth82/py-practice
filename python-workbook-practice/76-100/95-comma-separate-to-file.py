# Question: Enter the names as an input the comma separated entries. These entries should be written to a text file, each entry in a separate line

name=input('Enter the names of planets: ')

print(name)
#O/P: Jupiter,Neptune,Mars
print(type(name))
#O/P: <class 'str'>

names_list=name.split(',')
print(names_list)
# O/P: ['Pluto', 'Mars']

with open('names_file.txt', 'w') as name_write_file:
    name_write_file.write("\n".join(str(i) for i in names_list))

#### WORKS GREAT #####
    
##### ALTERNATIVE SOLN #####

line = input("Enter values: ")
line_list = line.split(",")
with open("user_data_commas.txt", "a+") as file:
    for i in line_list:
        file.write(i + "\n")

        







