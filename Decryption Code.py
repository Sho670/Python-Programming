# Here We are performing the decryption of the previous code i did for the encryption of the string.


t= input("Enter text:")

s= int(input("Enter shift:"))

for ch in encrypted:

  if ch.isalpha():
    
    decrypted += chr(ord(ch)-s)

  else:
    decrypted += ch


print("Decrypted:", decrypted)

#Excepted output:

#Input: Hello
#Output: khnoor

