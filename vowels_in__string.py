a=['A','E','I','O','U','a','e','i','o','u']
cnt=[]
b=list(input().split())
for i in b:
    for x in i:
        if x in a and x not in cnt:
            cnt+=[x]
if len(cnt)==0:print(-1)
else:print(*cnt)
