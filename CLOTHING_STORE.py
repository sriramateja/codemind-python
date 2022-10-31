a=input()
e=0
b=list(map(int,input().split()))
d=set(b)
for i in d:
    co=b.count(i)
    e+=co//2
print(e)