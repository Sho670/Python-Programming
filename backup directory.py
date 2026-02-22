# The following program aims to backing up a given Folder in which the folder should be working and present in a current working directory.

# The code defines the backing of that Folder into a ZIP File by using relevent modules and methods.

# The folder has to be created in the local folder. And also, the name of the folder should be the same used for the program used in the current code.

# The subfolders and the files are also has to be saved the Local Drive in the computer.


import os
import sys
import pathlib
import zipfile


directory = input("Enter Directory name that have to be backup:")

if not os.path.isdir (directory):
  print("Directory", directory, "does not exists")
  
  sys.exit(0)


currentDirectory = pathlib.Path(directory)

with zipfile.ZipFile("myZip.zip", node = "w") as archive:
  
  for file_path in currentDirectory.rglob("*"):
    archive.write(file_path,arcname= file_path.relative_to(currentDirectory))
  if os.path.isfile("myZip.zip"):
    print("Archive","myZip.zip"," file created successfully")
  else:
    print("Error in creating zip archive")
    
