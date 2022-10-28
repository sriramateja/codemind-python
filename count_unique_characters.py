a=input().lower()
c=[]
for i in a:
    if i!=' ':
        if a.count(i)==1:
            c+=[i]
if len(c)==0:print(0)
else:print(len(c))