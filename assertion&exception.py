import sys
def DivExp (a,b):
  assert a>0, "a should be greater than 0"
  try:
    c=a/b
  except ZeroDivisionError:
    print("Value of b cannot be zero")
    sys.exit(0)
  else:
    return c
