a=int(input())
b=list(map(int,input().split()))
c=[]
if a%2!=0:
    for i in range(a//2):
        z=-(i+1)
        c+=[b[i]]
        c+=[b[z]]
    c+=[b[(a//2)]]
    c+=[0]
    print(*c)
else:
    for i in range(a//2):
        z=-(i+1)
        c+=[b[i]]
        c+=[b[z]]
    print(*c)
        
        
        