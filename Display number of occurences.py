# This program shows to read a multi digit number and provide the fequency of every particular number.

# This is a very simple way to put the concept into the code of python.

# Here we are using "count" , which means that how many times the particular element is being repeated in the number.

n=input("Enter a number:")

print("The number is:",n)
D=set(n)

for ele in D:
  print(ele,"occurs",n.count(ele),"times")
