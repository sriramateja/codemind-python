a=int(input())
b=list(map(int,input().split()))
c=sum(b)//a
cnt=0
for i in b:
    if i>=c:
        cnt+=1
print(cnt)