a=input()
b=list(map(int,input().split()))
c=[]
for i in  b:
   if i not in c:
       d=b.count(i)
       if d==i:
           c+=[d]
if len(c)==0:
    print(-1)
else:
    print(*c)
