# Here we are learning about palindrome of an number.

# A palindrome number is  a number that stays the same when you reverse the digits.

# Example: 3113, 1221, 454

n =3113

original = n

r=0

while n>0:
  d=n%10
  r=(r*10)
  n//=10

if original ==r:
  print("True")
else:
  print("False")
  
