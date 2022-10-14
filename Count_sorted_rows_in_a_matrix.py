a,b=map(int,input().split())
cnt=0
for i in range(a):
    b=list(map(int,input().split()))
    c=sorted(b)
    d=c[::-1]
    if c==b or d==b:
        cnt+=1
print(cnt)