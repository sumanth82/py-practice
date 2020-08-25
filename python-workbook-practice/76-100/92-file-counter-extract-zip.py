#Question: Please download the attached ZIP file and extract its files in a folder. Then, write a script that counts 
# and prints out the number of .py files in that folder.
#Expected output: 
#2

import os
import zipfile
from zipfile import *

file_name='files.zip'

print(os.listdir('.'))

# O/P: Lists all the files in this dir 

# ['new_countries_missing.txt', 'names_file.txt', '76-current-date-n-time.py', '78-random-password-gen.py', 'countries_clean.txt', '88-Data-filter_2.py', 'countries_by_area.txt
#', '95-comma-separate-to-file.py', '81-username-n-password-checker.py', '85-data-cleaner.py', 'countries_missing_fixed.txt', '82-distance-calculator.py', 'file-writer.py', '9
#7-advanced-file-writer.py', 'advanced-file-write.txt', 'countries_missing.txt', '92-file-counter.py', '87-Add-missing-data.py', 'countries-raw.txt', '80-Advanced-password-che
#cker.py', '86-Data-checker.py', '79-Password-checker.py', 'files', '88-Data_filter.py', 'files.zip', 'users.txt', '77-Year-of-birth-calculator.py', 'tmp', '96-file-writer.py'
#, 'countries_raw.txt']

data_zip = zipfile.ZipFile('files.zip', 'r')
data_zip.extractall(path='files/')

#O/P: Extracts all the files in 'files.zip' to files/ folder 

file_list = os.listdir('./files')
print(file_list)

# O/P: ['file2.txt', 'file1.txt', 'file5.txt', 'file3.py', 'file4.py']

count=0
for i in file_list:
    if i.endswith('.py'):
      count+=1
      
print(count)

# O/P: 2

#### WORKS GREAT #####

##### ALTERNATIVE SOLUTION #####

import glob
 
file_list=glob.glob1("files","*.py")
print(len(file_list))

# O/P: 2




