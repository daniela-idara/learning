
# - Create new directory
# - Creates a text file in that directory
# - Writes in the file a list of all the files in the directory
# - Give total byte count of those files

import os 
from os import path


os.mkdir("Results") # make directory 

bytes = 0 # placeholder for folder content size in bytes

folderpath = os.path.abspath(os.getcwd())
# print(folderpath)

# calculate size and redefine bytes
for path, dirs, files in os.walk(folderpath):
    for f in files:
        fp = os.path.join(path, f)
        bytes += os.path.getsize(fp)

myfile = open("Results/challengeresults.txt", "w+") # make file
# print("Item exists", str(path.exists("Results/challengeresults.txt"))) # check that it exists

myfile.writelines(["Total bytecount: ", str(bytes), "\n"])

myfile.write("Files list:\n--------------\n")

files = os.listdir() # prints list of files
for f in files:
     myfile.write(f + "\n") # creates list of files and puts in the .txt
     
     
myfile.close()
