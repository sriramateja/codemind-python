a,b=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in a:
    if i not in b:c+=[i]
for i in b:
    if i not in a:c+=[i]
print(*c)
    

