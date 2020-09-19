import pandas
 
data = pandas.read_csv("countries_by_area.txt")
data["density"] = data["population_2013"] / data["area_sqkm"]
data = data.sort_values(by="density", ascending=False)
 
for index, row in data[:5].iterrows():
    print(row["country"])

''' Explanation:

We're using pandas to load the data as a dataframe and then calculate a density column in line 4. 
Then we use sort_values  to sort the data by density in descending order. 
Lastly in the last two lines we access the first 5 rows of the dataframe and iterate using iterrows.

'''

# O/P:

#India
#Pakistan
#Nigeria
#China
#Indonesia

