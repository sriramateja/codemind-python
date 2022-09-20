def pri(n):
    if n=='1':
        return 0
    cnt=0
    n=int(n)
    for i in range(2,(n//2)+1):
        if n%i==0:
            cnt+=1
            return 0
    return 1
a=int(input())
if a%2==0 or a%3==0 or a%4==0 or a%5 ==0 or a%6==0 or a%7==0 or a%8==0 or a%9==0 :
    print('Not Mega Prime')
else:
    z=str(a)
    x=1
    for i in z:
        b=pri(i)
        x=b*x
    if x:print('Mega Prime')
    else:print('Not Mega Prime')

    