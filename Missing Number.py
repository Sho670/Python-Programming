#Leetcode Question 268( Missing Number)

class Solution:
  l =len(nums)
  for i in range(0,l+1):
    if i not in nums:
      return i


# Time Complexity: O(n^2)

#Another method. Optimized

l=len(nums)
nsum= l*(l+1)//2

s=sum(nums)

return nsum-s

# Time Complexity : O(n)
