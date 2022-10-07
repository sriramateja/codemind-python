def ispalin(j):
    j=str(j)
    d=j[::-1]
    if d==j:
        return True
    return False
a=int(input())
b=int(input())
c=[]
for i in range(a,b+1):
    if ispalin(i):
        c+=[i]
print(*c)