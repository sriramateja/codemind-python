c=[]
a=input()
b=list(map(int,input().split()))
for i in b:
    if b.count(i)==1:c+=[i]
if len(c)==0:print(-1)
else:print(*c)