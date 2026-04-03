# In this program we will be sorting the given text file above with some sorting methods..

# The sorting function we are going to use is sort() function !!

import os.path

import sys

filename=input("Enter the filename given above:") #SAMPLE TEXT FILE ATTACHED

if not os.path.isfile(filename):
  print("File",filename,"doesnot exists")
  sys.exit(0)

infile=open(filename, "r")
myList=infile.readlines()

lineList=[]
for line in myList:
  lineList . append(line.strip())
lineList.sort()

# Writing sorted contents to new file sorted.txt
