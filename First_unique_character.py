a=input()
c=[]
for i in a:
    if a.count(i)==1:
        c+=[i]
        break
if len(c)==0:print(-1)
else:print(*c)