# Leetcode Question = Single Number

class Solution:

a=[1,1,2,2,3,3,1]
d={}
for i in a:
  if l in d:
    d[i]=d[i]+1
  else:
    d[i]=1
for i in d:
  print(i,"-",d[i])

