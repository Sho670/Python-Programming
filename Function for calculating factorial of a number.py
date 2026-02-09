# This is a sample program to calculate factorial of a number using any number.
# Also, the number should not be a negative number because it may not bring the factorial of that number. And the condition is being also written in the print statement

# Also this program is designed to compute a binomial coefficient as well. So, that we can get both the outputs.

def fact(num):
  if num==0:
    return 1
    
  else:
    return num*fact(num-1)
    
a=int(input("Enter value of N:"))

b=int(input("Enter value of b, which should not be negative :"))

aCb=fact(a)/(fact(b)*fact(a-b))

print(a,'C',r,"=","d"%aCb,sep="")

print("Note: The number which is to be given should not be a negative number.")
