def ispalin(x):
    y=x[::-1]
    y=int(y)
    y=str(y)
    if y==x:return True
    return False
a=input()
cnt=0
b=list(input().split())
for i in b:
    if ispalin(i):cnt+=1
print(cnt)
