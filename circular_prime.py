def prime(n):
    n=int(n)
    for i in range(2,n):
        if n%i==0:
            return False
    return True

a=input()
b=a[::-1]
c=prime(a)
d=prime(b)
if c and d:
    print('circular prime')
elif c or d:
    print('prime but not a circular prime')
else:print('not prime')