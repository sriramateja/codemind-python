a=input()
c=0
b=list(map(int,input().split()))
for i in b:
    if i%2==0:
        c+=i
print(c)
    