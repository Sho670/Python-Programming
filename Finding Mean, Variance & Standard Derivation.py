# This is to figure out the mean, variance and standard derivation of the data provided by the user.

# Concept: The element number will be provided from the user, and hence it will read numbers from the console so that it can create a list out of it.

# Also, providing some messages related to that.

from math import sqrt

console = []

num= int(input("Enter the number of elements in the list:"))

for i in range(num):
  element = int(input("Enter the element:"))
  console.append(element)
print("The length of list is",len(console))

print("Listing the Contents:", console)

count = 0
for elem in console:
  count += (elem-mean) * (elem-mean)

variance = count/num

std = sqrt(variance)

print("Mean is:",mean)

print("Variance is:",variance)

print("Standard Derivation is :", "%.2f"%stdDev)
