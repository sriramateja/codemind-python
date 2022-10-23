a=input()
b=list(map(int,input().split()))
c,d=map(int,input().split())
e=[]
for i in b:
    if i>=c and i<=d:e+=[i]
if len(e)==0:print(-1)
else:print(min(e))