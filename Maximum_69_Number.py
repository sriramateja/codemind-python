a=input()
b=list(a)
for i in range(len(a)):
    if b[i]=='6':
        b[i]='9'
        break
c=''
for j in b:
    c+=j
print(c)