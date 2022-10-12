a=input()
b=list(map(int,input().split()))
c=[]
for i in b:
    if i not in c:
        c+=[i]
print(*c)