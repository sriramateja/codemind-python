a=input().lower()
b=input().lower()
c=[]
for i in b:
    if i!=' ':
        if i in a and i not in c:c+=[i]
print(len(c))