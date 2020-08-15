#Question: Please take a look at the following list:
#checklist = ["Portugal", "Germany", "Munster", "Spain"]
#One of the items is not a country. Please use Python and the file containing the list of countries (attached) as data source to filter out the checklist  of non-country items. Once you have filtered out checklist , then print it out.

#Expected output: 

#['Germany', 'Portugal', 'Spain']

checklist = ["Portugal", "Germany", "Munster", "Spain"]

print(checklist[0])
#O/P: Portugal
print(type(checklist[0]))
#O/P: str

new_checklist=[]
for x in checklist:
    x=x+'\n'
    #print(x)
    #print(type(x))
    new_checklist.append(x)

print(new_checklist)
# O/P: ['Portugal\n', 'Germany\n', 'Munster\n', 'Spain\n']

with open('countries_clean.txt', 'r') as file:
    a=file.readlines()
    #print(a)

new_list=[]

for i in a:
    if i in new_checklist:
        new_list.append(i)
    else:
      continue

print(new_list)

# O/P: ['Germany\n', 'Portugal\n', 'Spain\n'] 
## WORKS GREAT!!!!!

####################   ALTERNATIVE SOLUTION #################

checklist = ["Portugal", "Germany", "Munster", "Spain"]
 
with open("countries_clean.txt", "r") as file:
    content = file.readlines()
 
content = [i.rstrip('\n') for i in content]
checked = [i for i in content if i in checklist]
 
print(checked)
# O/P: ['Germany', 'Portugal', 'Spain']
