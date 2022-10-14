a,b=map(int,input().split())
cnt=cnt1=su=0
for i in range(a):
    b=list(map(int,input().split()))
    cnt+=1
    if cnt==1 or cnt==a:pass
    else:
        c=b[0]
        d=b[-1]
        for i in b:
            if i!=c and i!=d:
                su+=i
print(su)
   
   
    