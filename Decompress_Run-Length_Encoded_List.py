def form(e,f):
    c=[]
    for i in range(e):
        c+=[f]
    return c
c=[]
a=int(input())
b=list(map(int,input().split()))
for i in range(a):
    if i%2==0:
        x=i+1
        e,f=b[i],b[x]
        c+=form(e,f)
print(*c)
