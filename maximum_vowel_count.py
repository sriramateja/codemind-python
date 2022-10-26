a=input().split()
b=['a','e','i','o','u']
c,cnt=[],0
for i in a:
    for x in i:
        if x in b:
            cnt+=1
    c+=[cnt]
    cnt=0
mi=max(c)
print((mi))