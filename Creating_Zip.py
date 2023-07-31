import os
from zipfile import ZipFile

foldername = input("Enter the folder name: ")
files = os.listdir(foldername)
with ZipFile('test.zip','w') as z:
    for i in files:
        z.write(os.path.join(foldername, i))

