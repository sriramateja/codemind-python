def prime(x):
    if x<2:return False
    for i in range(2,x//2+1):
        if x%i==0:return False
    return True
a=int(input())
b=list(map(int,input().split()))
d=0
for i in b:
    if prime(i):d+=1
print(d)

