a,b=map(int,input().split())
e=[]
for i in range(a):
    c=sum(list(map(int,input().split())))
    e+=[c]
print(max(e))