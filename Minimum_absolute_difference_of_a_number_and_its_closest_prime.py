def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
a=int(input())
c=[]
g=[]
cnt=0
for j in range(a,a*2):
    cnt-=1
    z=a+cnt
    e=prime(j)
    f=prime(z)
    if e:
        if len(c)==1:
            break
        else:
            c+=[j]
    elif f:
        if len(g)==1:
            break
        else:
            g+=[z]

h=abs(a-c[0])
i=abs(a-g[0])
print(min(h,i))
