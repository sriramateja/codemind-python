a,b=map(int,input().split())
su=0
su1=0
for i in range(a):
    if i%2==0:
        b=sum(list(map(int,input().split())))
        su+=b
    else:
        c=sum(list(map(int,input().split())))
        su1+=c
print(su,su1)