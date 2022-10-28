a=input().lower()
c=[]
for i in a:
    if i!=' ' and i not in c:
        c+=[i]
d=sorted(c)
print(len(d))