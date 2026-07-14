# Leetcode 169 (Name: Majority Element)

# MAjority elements means apperaing more than 6 times half time  

# Formula [n]/2

a=[1,1,2,2,3,3,1]

d={}
for i in a :
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
for i in d:
  if d[i]>=len(a)/2:
    
    print(i,"-",d[i])


# Keeping the same code as leetcode question 132. 
# Only changes is that, after the for i condtion for d, we are using a condition of d[i] being greater than the len of a with division of 2
