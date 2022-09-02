from random import*
x=int(input("vvedite x:"))
y=int(input("vvedite y:"))
n=10
a=[0]*n
for i in range(n):
    a[i]=randint(x,y+1)
    print("a[",i,"]:",a[i])
