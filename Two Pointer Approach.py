# Considering a array of certain elements. We are here to figure out the maximum profit from the array.

# Approach: Two Pointer Approach

arr = [15,3,2,1,6,11,8]

arrlen = len(arr)

maxprofit=0
minvalue=arr[0]

for i in range(arrlen):
  if arr[i] < minvalue:
    minvalue = arr[i]
  profit = arr[i]-minvalue

  if profit> maxprofit:
    maxprofit=profit

print("Maximum Profit: {maxprofit}")


# Explanation Steps:

# Step 1: First find first pointer
# Step 2: Second find second pointer
# Step 3: Finding difference between first and second pointer
