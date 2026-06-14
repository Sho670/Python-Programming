# Bubble Sorting In Python Programming

def bubble(arr):

# Taking the length of the array provided by user
  num=len(arr)

  for i in range(num):

    swap=False
    
#Conditions Starts

    
    for j in range(0,n-i-1):
      if arr[j]>arr[j+1]:
        arr[j],arr[j+1]=arr[j+1],arr[j]

        swap=True

    if  not swap:
      break


return arr

# Getting inputs from the user

numbers=input("Enter bunch of numbers:").split()

print("Original  List:",numbers)

sortedlist=bubble(numbers)

print("Sorted list::", sortedlist)
