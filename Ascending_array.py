a=int(input())
b=list(map(int,input().split()))
cnt=0
for i in range(1,a):
    if b[i]>b[i-1]:cnt+=1
if cnt==a-1:print('yes')
else:print('no')
    