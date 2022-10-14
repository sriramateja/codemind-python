a,b=map(int,input().split())
cnt=su=0
for i in range(a):
    b=list(map(int,input().split()))
    cnt+=1
    if cnt==1 or cnt==a:
        su+=sum(b)
    else:
        c=b[0]
        d=b[-1]
        su+=c+d
print(su)
   
   
    