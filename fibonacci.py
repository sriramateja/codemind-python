a=int(input())
b,c=0,1
d=[b,c]
for i in range(a-2):
    e=b+c
    d+=[e]
    c=e
    b=d[-2]
print(*d)
    

    
    
    
    