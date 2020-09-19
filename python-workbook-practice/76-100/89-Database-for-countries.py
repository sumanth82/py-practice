# Download the database file - database.db (database.zip) ; The file contains a table with 50 country names along with their area in square km and population
# Use Python to print out those countries that have an area of > 2,000,000 sq kms. 

## ALTERNATIVE SOLN 

import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute("SELECT country FROM countries WHERE area >= 2000000")
rows=cur.fetchall()
conn.close()

for i in rows:
    print(i[0])


# country - Name of the column
# countries - Name of a table in a database


# O/P: 

#Russia
#Canada
#United States of America
#China
#Brazil
#Australia
#India
#Argentina
#Kazakhstan
#Algeria
#Congo Dem Rep of the
#Greenland
#Saudi Arabia

