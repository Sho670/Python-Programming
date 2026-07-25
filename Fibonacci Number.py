# Leetcode 509 (Fibonacci Number)

# The Fibonacci Series works with the approach of adding the present number with the previous number and continuoes forever !!

n=1
def fib(n):

  if n==0:
    return 0
    
  if n==1:
    return 1

  return fib(n-1)+fib(n-2)

# Output Expected: 0 1 1 2 3 4 5
