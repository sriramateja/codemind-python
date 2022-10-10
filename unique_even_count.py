a=input()
cnt=0
b=list(map(int,input().split()))
c=set(b)
for i in c:
    if i%2==0:
        cnt+=1
print(cnt)