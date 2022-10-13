a=input()
b=list(map(int,input().split()))
c=0
d=0
e=[]
for i in b:
    if i%2==0:c+=1
    else:d+=1
e+=[c]
e+=[d]
print(*e)
