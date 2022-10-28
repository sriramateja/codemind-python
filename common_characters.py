a=input().lower()
b=input().lower()
c=''
for i in a:
    if i!=' ':
        if i in b and i not in c:c+=i
d=sorted(c)
if len(d)==0:print(-1)
else:
    print(''.join(d))
    