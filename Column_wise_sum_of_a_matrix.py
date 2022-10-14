a,b=map(int,input().split())
e=[]
su=0
c=[list(map(int,input().split())) for i in range(a)]
for i in range(b):
    for x in range(a):
        s=c[x][i]
        su+=s
    e+=[su]
    su=0
print(*e)