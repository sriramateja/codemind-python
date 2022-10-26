a=int(input())
b=list(map(int,input().split()))
cnt=0
for i in range(1,a):
    if i==a-1:break
    if b[i]%2==0:
       if b[i-1]%2==0:
            if b[i+1]%2==0:cnt+=1
print(cnt)