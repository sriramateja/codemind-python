a=input()
b=list(map(int,input().split()))
c=set(b)
cnt=0
for i in c:
    if i%2==0:
        cnt+=i
print(cnt)