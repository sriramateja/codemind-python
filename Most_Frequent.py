a=input()
b=list(map(int,input().split()))
g=list(set(b))
d=e=[]
for i in g:
    f=b.count(i)
    d+=[f]
ma=max(d)
z=d.index(ma)
x=g[z]
print(x)
    
    