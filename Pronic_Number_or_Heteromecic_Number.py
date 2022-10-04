a=int(input())
c=0
for i in range(1,a):
    z=i+1
    if i*z==a:
        c=1
        break
if c==1:print('YES')
else:print('NO')
    