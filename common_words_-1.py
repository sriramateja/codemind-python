a=input().split()
b=input().split()
cnt=0
for i in a:
    if i in b:cnt+=1
    else:
        x=i.lower()
        y=i.upper()
        if x in b or y in b:cnt+=1
print(cnt)