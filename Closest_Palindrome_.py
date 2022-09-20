a=int(input())
x=[]
for i in range(a+1,a*2):
    z=a-(i-a)
    z=str(z)
    if z[::-1]==z:
        x+=[z]
    i=str(i)
    b=i[::-1]
    if i==b:
        x+=[i]
    if len(x)==2:break
y=abs(a-int(x[0]))
c=abs(a-int(x[1]))
if y==c:
    print(*x)
elif y<c:
    print(x[0])
else:print(x[1])
    
    
    
    

        