a=input()
b=list(map(int,input().split()))
c=[]
for i in b:
    if i not in c:
        d=b.count(i)
        if d==i:
            c+=[i]
if len(c)==0:
    print(-1)
else:
    print('{:.2f}'.format(sum(c)/len(c)))
    