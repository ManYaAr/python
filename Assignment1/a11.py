n=int(input("enter the number:"))
a=0
b=1
for i in range(n+1):
    c=b+a
    a=b
    b=c
    print(c)
