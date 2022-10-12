def palin(x):
    x=x.lower()
    y=x[::-1]
    if y==x:
        return True
b=list(input().split())
d=0
for i in b:
    c=palin(i)
    if c:d+=1
print(d)
    