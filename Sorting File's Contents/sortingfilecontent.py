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
# From this point, all the sorted content from the initial Text File which the file attached with the code, will be now stored in the sorted file...

outfile = open("sorted.txt", "w")

for line in lineList:
  outfile.write(line + "\n")

infile.close()
# Closing the input file

outfile.close()
# Closing the output file

if os.path.isfile("sorted.txt"):
  print("\n File Containing sorted content sorted.txt created successfully !!!")
  print("Sorted.txt contains", len(lineList), "lines")
  print("Contents of sorted.txt")
  print("====================================================================")
  
# The above lines is only for putting a division between the printed statements and the following up Text File !!!

readFile = open("sorted.txt","r")

for line in readFile:
  print(line, end= "")


# END OF THE CODE !!!!!!!!!


# EXPECTED OUTPUT:

# Enter the filename given above: TEXTFILE.txt
# File Containing sorted content sorted.txt created successfully !!!
# Sorted.txt contains 10 lines
# Contents of sorted.txt

#=========================================================================

# THE SORTED TEXT FILE # 
