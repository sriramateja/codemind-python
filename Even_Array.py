a=input()
b=list(map(int,input().split()))
c=True
for i in b:
    if i%2!=0:
        c=False
        break
print(c)