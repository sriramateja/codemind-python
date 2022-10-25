def iswave(a,b):
    for i in range(1,a-1):
        if b[i]>b[i-1]:
            if b[i]<b[i+1]:return False
        elif b[i]<b[i-1]:
            if b[i]>b[i+1]:return False
    return True
a=int(input())
b=list(map(int,input().split()))
if iswave(a,b):print('yes')
else:print('no')