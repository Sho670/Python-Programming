# Leetcode Question 152 (Maximum Product SubArray)

def maximumproductsubarray(self, list -> int):

h=1
l=1
ah=1
al=1



m= max(nums)

for i in nums:
  h = i*ah
  l = i*al
  ah = max(h,l,i)
  al = min(h,l,i)


  if m < ah:
    m = ah


  return m

  
