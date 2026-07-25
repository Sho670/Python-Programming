# Here we are learning about palindrome of an number

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
  
