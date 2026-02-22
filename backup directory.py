
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
    
