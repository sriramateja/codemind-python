a=int(input())
b=list(map(int,input().split()))
c=[]
d=[]
for i in range(1,a,2):
    f=i-1
    c+=[b[i]]
    d+=[b[f]]
e=[]
m=0
for x in d:
    n=c[m]
    for z in range(n):
        e+=[x]
    m+=1
print(*e)