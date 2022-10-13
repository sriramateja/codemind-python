a=input()
b=list(input().split())
c=''
e=[]
for i in b:
    c+=i
d=str(int(c)+1)
for i in d:
    e+=[i]
print(*e)