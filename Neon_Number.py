a=int(input())
b=a**2
su=0
for i in str(b):
    i=int(i)
    su+=i
if su==a:print('Neon Number')
else:print('Not Neon Number')