a=int(input())
b=list(map(int,input().split()))
c=sum(b)
if c//a in b:
    print(True)
else:print(False)
