a=input()
b=list(map(int,input().split()))
c=int(input())
d=[]
for i in b:
    if i not in d:
        e=b.count(i)
        if e==c:
            d+=[i]
if len(d)==0:
    print(-1)
else:
    print(*d)