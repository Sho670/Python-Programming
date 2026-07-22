# Encryption of string in python programming !!

t = input("Enter Text")

s= int(input("Enter shift:"))

encrypted = ""

for ch in t:
  
  if ch.isalpha():
    encrypted+= chr(ord(ch)+s)
    
  else:
    encrypted += ch


print("Encrypted :", encrypted)

#Expected Output:

#Input: Hello

#Output: knoor

