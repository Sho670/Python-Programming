# Bubble Sorting In Python Programming

def bubble(arr):

# Taking the length of the array provided by user
  num=len(arr)

  for i in range(num):


  
#Conditions of swapping starts from here
    
    swap=False
    
    
    for j in range(0,n-i-1):
      if arr[j]>arr[j+1]:
        arr[j],arr[j+1]=arr[j+1],arr[j]

        swap=True


# If the swapping not possible after a , then break the loop
    
    if  not swap:
      
      break

return arr

# Getting inputs from the user

numbers=input("Enter bunch of numbers:").split()


# Prints the original list provided from the user

print("Original  List:",numbers)

sortedlist=bubble(numbers)

# Prints the sorted list after the sorting process completes 
print("Sorted list::", sortedlist)
