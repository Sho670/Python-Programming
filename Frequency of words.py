
# This program display's the frequency of the words in a file.

# As of now you can print the 10 most frequent words from it.

# Here we are using some import fuctions also for better and easy access.

import sys/*-q
import string
import os.path

name=input("Enter the file name saved:")

if not os.path.isfile(name):
  print("File",name,"doesn't exists")
  sys.exit(0)

ifile=open(name,"r")
filecont=""

for sentence in ifile:
  for ch in line:
    if ch not in string.punctuation:
      filecont=filecont + ch
    else:
      filecont=filecont + ''
  
  wordF = {}
  wordList = filecont.split()


#Calculating the Frequency of the particular words

for word in wordList:
  if word not in wordF.keys():
    wordF[word] = 1
  else:
    wordF[word] += 1

sortWord = sorted(wordF.items(),key = lambda x:x[1], reverse= True)

# Now we have to display the most frequent words
#Final step

print("Most Frequent words are:")
for i in range(10):
  print(sortWord[i][0], "occurs", sortWord[i][1], "times")

print("End of Output..........")
