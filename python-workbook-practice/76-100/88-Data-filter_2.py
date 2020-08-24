#Question: Create a script that uses the attached countries_by_area.txt  file as data source and prints out the top 5 most densely populated countries
#Expected output: 

#India
#Pakistan
#Nigeria
#China
#Indonesia

import pandas

from pandas import DataFrame

with open('countries_by_area.txt', 'r+') as file:
    df=pandas.read_table(file, delimiter=',')
    print(df)


# O/P: 
#rank                   country  area_sqkm  population_2013
#0      1                    Russia   17075200        142833689
#1      2                    Canada    9984670         35181704
#2      3  United States of America    9826630        320050716
#3      4                     China    9596960       1385566537
#4      5                    Brazil    8511965        200361925
#5      6                 Australia    7686850         23342553
#6      7                     India    3287590       1252139596
#7      8                 Argentina    2766890         41446246
#8      9                Kazakhstan    2717300         16440586
#9     10                   Algeria    2381740         39208194
#10    11      Congo Dem Rep of the    2345410         67513677
#11    12                 Greenland    2166086            56987
#12    13              Saudi Arabia    2149690         28828870
#13    14                    Mexico    1972550        122332399
#14    15                 Indonesia    1919440        249865631
#15    16                     Sudan    1844729         37964306
#16    17                     Libya    1759540          6201521
#17    18                      Iran    1648000         77447168
#18    19                  Mongolia    1564116          2839073
#19    20                      Peru    1285220         30375603
#20    21                      Chad    1284000         12825314
#21    22                     Niger    1267000         17831270
#22    23                    Angola    1246700         21471618
#23    24                      Mali    1240000         15301650
#24    25              South Africa    1219912         52776130
#25    26                  Colombia    1138910         48321405
#26    27                  Ethiopia    1127127         94100756
#27    28                   Bolivia    1098580         10671200
#28    29                Mauritania    1030700          3889880
#29    30                     Egypt    1001450         82056378
#30    31                  Tanzania     945087         49253126
#31    32                   Nigeria     923768        173615345
#32    33                 Venezuela     912050         30405207
#33    34                   Namibia     825418          2303315
#34    35                  Pakistan     803940        182142594
#35    36                Mozambique     801590         25833752
#36    37                    Turkey     780580         74932641
#37    38                     Chile     756950         17619708
#38    39                    Zambia     752614         14538640
#39    40           Myanmar (Burma)     678500         53259018
#40    41               Afghanistan     647500         30551674
#41    42               South Sudan     644329         11296173
#42    43                    France     643427         64291280
#43    44                   Somalia     637657         10495583
#44    45  Central African Republic     622984          4616417
#45    46                   Ukraine     603700         45238805
#46    47                  Botswana     600370          2021144
#47    48                Madagascar     587040         22924851
#48    49                     Kenya     582650         44353691
#49    50                     Yemen     527970         24407381

