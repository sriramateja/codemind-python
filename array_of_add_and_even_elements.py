a=input()
b=list(map(int,input().split()))
c1=c2=[]
c3=len(b)
c4=0
for i in b:
    if i%2==0:
        i=str(i)
        c1=c1+[i]
    else:
        i=str(i)
        c2=c2+[i]
print(*c2+c1)