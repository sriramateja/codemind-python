a=int(input())
b=list(map(int,input().split()))
c,d=[],[]
for i in b:
    if i not in c:
        c+=[i]
        d+=[i]
        d+=[b.count(i)]
print(*d)
        