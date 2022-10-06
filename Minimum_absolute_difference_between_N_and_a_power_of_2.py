a=int(input())
if a==1:
    print(1)
else:
    cnt=0
    b=[]
    for i in range(1,a+1):
        c=2**i
        if c<a:
            b+=[c]
        elif c==a:
            cnt=1
            break
        elif c>a:
            b+=[c]
            break
    if cnt==1:
        print(0)
    else:
        s=abs((a-b[-2]))
        f=abs((a-b[-1]))
        print(min(s,f))