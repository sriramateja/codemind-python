a=int(input())
b=list(map(int,input().split()))
c=d=0
cnt=0
e=a//2
for i in b:
    cnt+=1
    if cnt<=e:
        c+=i
    else:
        d+=i
print(c)
print(d)
    
    