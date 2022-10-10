a=input()
b=list(map(int,input().split()))
c=True
d=-1
for i in b:
    d+=1
    if i%2!=0:
        if d%2!=0:
            c=True
        else:
            c=False
            break
print(c)
    