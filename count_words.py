a=input().split()
cnt=0
b=['A','E','I','O','U','a','e','i','o','u']
for i in a:
    if i[0] in b and i[-1] not in b:
        cnt+=1
print(cnt)