a=input("enter the first string:")
b=input("enter the second string:")
if len(a)==len(b):
    if sorted(a)==sorted(b):
        print(a,"and",b,"are anagrams")
    else:
         print(a,"and",b,"are not anagrams")
else:
    print(a,"and",b,"are not anagrams")