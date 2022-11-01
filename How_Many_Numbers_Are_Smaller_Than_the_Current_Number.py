def ad(i,b):
    cnt=0
    for z in b:
        if i>z:cnt+=1
    return cnt
a=input()
c=[]
b=list(map(int,input().split()))
for i in b:
    d=ad(i,b)
    c+=[d]
print(*c)