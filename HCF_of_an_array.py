a=input()
cnt=0
b=list(map(int,input().split()))
c=b[0]
for i in b:
    if i%c==0:
        cnt+=1
if cnt==int(a):
    print(c)
else:print(1)

    