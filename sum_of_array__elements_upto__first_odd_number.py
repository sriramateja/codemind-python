a=input()
b=list(map(int,input().split()))
c=0
for i in b:
    if i%2!=0:
        break
    else:
        c+=i
print(c)
    