# Add countries in checklist to countries_missing.txt file

checklist=["Portugal", "Germany", "Spain"]

newline_checklist=[]

for i in checklist:
    i+='\n'
    newline_checklist.append(i)

print(newline_checklist)

#O/P: ['Portugal\n', 'Germany\n', 'Spain\n']

with open('countries_missing.txt', 'r') as file:
    a=file.readlines()
    new_checklist=str(a+checklist)

with open('new_countries_missing.txt', 'w') as newfile:
    #newfile.writelines(new_checklist) # This writes all string element into a single line
    newfile.writelines(a) # This writes a list object into a single line, for each list element
    # O/P:  Afghanistan
    #       Albania
    #       Algeria

with open('countries_missing.txt', 'a') as newfile:         # 'a' - Used to Append
    newfile.write('\n')                                     # Append a newline
    newfile.writelines(newline_checklist)                   # This writes a list object into a single line, for each list element  


############## ALTERNATIVE SOLUTION ##########


checklist=["Portugal", "Germany", "Spain"]

new_ardit_checklist=[]

for i in checklist:
    i+='\n'
    new_ardit_checklist.append(i)

print(new_ardit_checklist)

with open('countries_missing.txt', 'r') as file:
    content=file.readlines()

updated_list=sorted(new_ardit_checklist+content)

with open('countries_missing_fixed.txt', 'w') as file:
    for i in updated_list:
        file.write(i)









