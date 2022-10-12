a=int(input())
b=list(map(int,input().split()))
c=a//2
d=b[:c]
e=b[c:]
f=e[::-1]
print(*f+d)
