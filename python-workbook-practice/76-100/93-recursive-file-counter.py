#93 - Recursive File Counter
#Question: Please download the attached ZIP file - subdirs.zip. Inside the ZIP file there's a directory named subdirs. 
# That directory contains other directories inside. 
# Please write a script that counts the number of .py files contained inside subdirs and all its sub-directories.
#Expected output: 
#3

import os
import zipfile
import glob

zip_file=zipfile.ZipFile('subdirs.zip', 'r')
zip_file.extractall()   # If you don't specify the path it will unzip the zip file and put the files in the same foldername as the zipfile

# O/P: Creates a subdirs and all the files below that

list_of_files_n_folders = os.listdir('subdirs')
print(list_of_files_n_folders)

# O/P: ['level12', 'level11'] - Just displays the top level folders under subdirs

files = glob.glob('./subdirs/**/*.py', recursive=True) # This will list all the files with a specific match pattern under all the dir, sub-dirs
print(files)

# O/P: ['./subdirs/test.py', './subdirs/level12/level121/6.py', './subdirs/level12/level121/5.py', './subdirs/level11/4.py']

count=0

for i in files:
    if i.endswith('py'):
        count+=1

print(count)

# O/P: 3

## WORKS GREAT ##

## ALTERNATIVE SOLN #####

print(len(files))

# O/P: 3

