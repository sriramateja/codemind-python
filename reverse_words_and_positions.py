a=list(input().split())
b=[]
for i in a:b+=[i[::-1]]
print(*b[::-1])