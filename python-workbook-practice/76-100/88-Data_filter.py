#Question: Create a script that uses the attached countries_by_area.txt  file as data source and prints out the top 5 most densely populated countries
#Expected output: 

#India
#Pakistan
#Nigeria
#China
#Indonesia

with open('countries_by_area.txt', 'r') as datafile:
    content=datafile.readlines()
    print(content)

    # O/P: ['\n', 'rank,country,area_sqkm,population_2013\n', '1,Russia,\t17075200,\t142833689\n', '2,Canada,\t9984670,\t35181704\n', 
    # '3,United States of America,\t9826630,\t320050716\n', '4,China,\t9596960,\t1385566537\n', '5,Brazil,\t8511965,\t200361925\n', 
    # '6,Australia,\t7686850,\t23342553\n'.....

with open('countries_by_area_new.txt', 'w') as datafile:
    for i in content:
        i[3].
    content=datafile.readlines()
    print(content)






