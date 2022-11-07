a=input()
c='x'
d=''
b=['a','e','i','o','u']
for i in a:
    if i in b:d+='V'
    else:d+='C'
for i in d:
    if c[-1]!=i:
        c+=i
print(c[1:])