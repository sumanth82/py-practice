#Question: Please download the attached urls.txt file. The file contains some broken URLs. Here's what the file contains:

#https:/www.google.com
#https:/www.yahoo.com
#https:/www.stackoverflow.com
#https:/www.pythonhow.com
#Please use Python to remove the "s" from "https" and add another forward slash next to the existing slash, so the content looks like in the expected output.

#Expected output: 

#http://www.google.com
#http://www.yahoo.com
#http://www.stackoverflow.com
#http://www.pythonhow.com

url_entry=[]
url_entry_modified=[]

with open('urls.txt', 'r') as url_file:
    for line in url_file:
        url_entry.append(line)
    print(url_entry)
    #O/P: ['https:/www.google.com\n', 'https:/www.yahoo.com\n', 'https:/www.stackoverflow.com\n', 'https:/www.pythonhow.com\n']

    for i in url_entry:
        #print(i)
        #print(type(i))
        i = i.replace(r'https:/', r'http://')
        url_entry_modified.append(i)
    
    print(url_entry_modified)

# O/P: ['http://www.google.com\n', 'http://www.yahoo.com\n', 'http://www.stackoverflow.com\n', 'http://www.pythonhow.com\n']

## WORKS GREAT AND as EXPECTED #####




