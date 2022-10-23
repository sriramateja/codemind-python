a=int(input())
b=list(map(int,input().split()))
c=[]
for x in range(1,a,2):
    f=b[x]
    for i in range(f):
        c+=[b[x-1]]
print(*c)
    


