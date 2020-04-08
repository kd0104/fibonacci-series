n=int(input("enter the number of terms:"))
a=0
b=1
for s in range(n):
  print(a)
  new=a
  a=b
  b=new+a ;
