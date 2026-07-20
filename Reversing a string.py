# Leetcode 344 (Reversing String)

# This is just a concept of two pointer way, where the left and right are taken in the whole array, and then the numbers are exchanged with their positions.

# After the all elements are exchanged, the string gets reversed, and prints as the output.



def reversestring(self,num):
  
  def f(left,right):
    
    if (left>=right):
      
      return
      s[left], s[right] = s[right], s[left]

      f(left +1, right-1)

      
      f(0,len(s)-1)
  
