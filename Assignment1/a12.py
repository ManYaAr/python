n=int(input("enter the number:"))
c=0
while n!=0:
    n=n//10
    r=n%10
    c=c+r
print("sum of digits:",c)