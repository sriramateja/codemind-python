a=['a','e','i','o','u']
cnt=[]
fi=[]
b=list(input().split())
for i in b:
    for x in i:
        if x  in a and x not in cnt:
            cnt+=[x]
if len(cnt)==len(a):print(0)
else:
    for i in a:
        if i not in cnt:fi+=[i]
    print(*fi)
    