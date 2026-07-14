#Leetcode Question 268( Missing Number)

class Solution:
  l =len(nums)
  for i in range(0,l+1):
    if i not in nums:
      return i
