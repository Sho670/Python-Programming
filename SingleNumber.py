# Leetcode Question = Single Number (No. 136)

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


#Another method of doing it

sum=0
for i in a:
  sum =sum ^ i
return sum
