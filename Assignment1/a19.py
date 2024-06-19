a=input("enter the string:")
p='''!@#$%^&*(){}:"<>?_-~'''
for i in a:
  if i in p:
    a=a.replace(i,"")
print(a)
