
import os
import sys
import pathlib
import zipfile


directory = input("Enter Directory name that have to be backup:")

if not os.path.isdir (directory):
  print("Directory", directory, "does not exists")
  sys.exit(0)


