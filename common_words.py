a=input().lower()
b=input().lower()
c=[]
a=a.split()
b=b.split()
for i in b:
    if i in a:c+=[i]
print(*c)
    