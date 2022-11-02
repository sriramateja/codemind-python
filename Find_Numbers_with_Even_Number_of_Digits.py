a=input()
c=0
b=list(input().split())
for i in b:
    if len(i)%2==0:c+=1
print(c)
