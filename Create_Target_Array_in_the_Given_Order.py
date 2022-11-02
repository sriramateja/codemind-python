e=[]
a=int(input())
b=list(map(int,input().split()))
c=int(input())
d=list(map(int,input().split()))
for i in range(a):
    x=d[i]
    y=b[i]
    e.insert(x,y)
print(*e)
    

