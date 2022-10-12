a=int(input())
b=list(map(int,input().split()))
c=set(b)
if sum(c)<=1:
    print('True')
else:
    print('False')