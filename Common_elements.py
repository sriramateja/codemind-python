a,b=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in a:
    if i in b and i not in c:
        c+=[i]
print(*c)

