# use database.db file, ten_more_countries.txt;
# Add the rows in this file to the database 

import sqlite3
import pandas

data = pandas.read_csv("ten_more_countries.txt")

conn = sqlite3.connect('database.db')
cur = conn.cursor()
for index, row in data.iterrows():
    print(row["Country"], row["Area"])
    cur.execute("INSERT INTO countries VALUES (NULL,?,?,NULL)",(row["Country"], row["Area"]))

# ?, ? will be replaced with the value of row["Country"] and row["Area"] respectively

conn.commit()
conn.close()

''' O/P:

Spain 499401
Turkmenistan 488100
Cameroon 469440
Papua New Guinea 451709
Uzbekistan 447400
Morocco 446301
Iraq 433970
Sweden 411621
Paraguay 397301
Japan 394744

'''