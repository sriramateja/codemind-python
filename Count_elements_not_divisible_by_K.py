a,b=map(int,input().split())
cnt=0
c=list(map(int,input().split()))
for i in c:
    if i%b==0:pass
    else:cnt+=1
print(cnt)