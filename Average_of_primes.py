def prime(x):
    if x<2:return False
    for i in range(2,x//2+1):
        if x%i==0:return False
    return True
a=input()
b=list(map(int,input().split()))
y=cnt=0
for i in b:
    if prime(i):
        cnt+=1
        y+=i
msg='{:.2f}'.format(y/cnt)
print(msg)
    
    