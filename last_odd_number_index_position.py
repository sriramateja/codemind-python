a=int(input())
b=list(map(int,input().split()))
for x in range(a):
    if b[x]%2==1:
        z=x
print(x)