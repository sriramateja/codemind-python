a=input()
b=list(map(int,input().split()))
c=[]
for i in b:
    c+=[i*i]
print(*sorted(c))