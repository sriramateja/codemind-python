b=list(input().split())
a=len(b)
d=[]
for i in range(a):
    if i%2==0:
        c=b[i]
        d+=[c[::-1]]
    else:
        d+=[b[i]]
print(*d)
    
    