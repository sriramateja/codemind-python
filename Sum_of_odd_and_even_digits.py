a=int(input())
e=d=0
b=list(map(int,input().split()))
for i in range(a):
    if i%2==0:
        e+=b[i]
    else:d+=b[i]
if abs(e-d)==0:print('YES')
else:print('NO')