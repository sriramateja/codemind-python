a=int(input())
b=list(input().split())
c=''
d=[]
for i in b:
    if i=='0':
        c=i+c
    else:
        c=c+i
print(*c)