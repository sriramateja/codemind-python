a=input()
b=list(map(int,input().split()))
c,e=map(int,input().split())
su=[]
for i in b:
    if i>=c and i<=e:
        su+=[i]
if len(su)==0:
    print(-1)
else:
    print(*su)

        