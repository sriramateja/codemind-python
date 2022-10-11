a=input()
b=list(map(int,input().split()))
c,e=map(int,input().split())
su=0
for i in b:
    if i>=c and i<=e:
        su+=i
print(su)

        