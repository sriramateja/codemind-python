a=input()
b=list(map(int,input().split()))
c=[]
for i in b:
    i=str(i)
    d=i[::-1]
    d=int(d)
    c+=[d]
print(*c)