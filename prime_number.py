a=int(input())
cnt=0
for i in range(2,a):
    if a%i==0:
        cnt+=1
        break
if cnt==1:print('not a prime')
else:print('prime')
        