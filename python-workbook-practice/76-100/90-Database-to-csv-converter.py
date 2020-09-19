# Download the database file - database.db (database.zip) ; The file contains a table with 50 country names along with their area in 
# square km and population
# Use Python to access the database table rows that have an area of > 2,000,000 sq kms. 
# Export these rows to a csv file

import sqlite3
import pandas

conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute("SELECT * FROM countries WHERE area >= 2000000")
rows=cur.fetchall()
conn.close()

print(rows)

# O/P: [(1, 'Russia', 17075200, 142833689), (2, 'Canada', 9984670, 35181704), (3, 'United States of America', 9826630, 320050716), (4, 'China', 9596960, 1385566537), (5, 'Brazil', 8511965, 200361925), (6, 'Australia', 7686850, 23342553), (7, 'India', 3287590, 1252139596), (8, 'Argentina', 2766890, 41446246), (9, 'Kazakhstan', 2717300, 16440586), (10, 'Algeria', 2381740, 39208194), (11, 'Congo Dem Rep of the', 2345410, 67513677), (12, 'Greenland', 2166086, 56987), (13, 'Saudi Arabia', 2149690, 28828870)]


df = pandas.DataFrame.from_records(rows)
df.columns=["Rank", "Country", "Area", "Population"]
print(df)

df.to_csv("countries_big_area.csv", index=False)

''' O/P:


    Rank                   Country      Area  Population
0      1                    Russia  17075200   142833689
1      2                    Canada   9984670    35181704
2      3  United States of America   9826630   320050716
3      4                     China   9596960  1385566537
4      5                    Brazil   8511965   200361925
5      6                 Australia   7686850    23342553
6      7                     India   3287590  1252139596
7      8                 Argentina   2766890    41446246
8      9                Kazakhstan   2717300    16440586
9     10                   Algeria   2381740    39208194
10    11      Congo Dem Rep of the   2345410    67513677
11    12                 Greenland   2166086       56987
12    13              Saudi Arabia   2149690    28828870

'''

