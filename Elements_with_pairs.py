a=int(input())
b=list(map(int,input().split()))
if a%2!=0:b+=[0]
print(*b)