a,b=map(int,input().split())
su=0
e=[]
c=[list(map(int,input().split())) for i in range(a)]
for x in range(b):
    for y in range(a):
        d=c[y][x]
        su+=d
    e+=[su]
    su=0
print(max(e))


