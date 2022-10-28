a=input().lower()
c=[]
for i in a:
    if i!=' ':
        if a.count(i)==1:
            c+=[i]
d=sorted(c)
print(''.join(d))