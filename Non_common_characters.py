a=input().lower()
b=input().lower()
c=[]
if len(a)>len(b):
    x=a
    y=b
else:
    x=b
    y=a
for i in x:
    if i!=' ':
        if i not in y  and i not in c:c+=[i]

for i in y:
    if i!=' ':
        if i not in x  and i not in c:c+=[i]
e=(sorted(c))
print(len(e))