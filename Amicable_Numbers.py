def check(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    return s
a=int(input())
b=int(input())
c=check(a)
d=check(b)
if c==b:print('Amicable')
else:print('Not Amicable')