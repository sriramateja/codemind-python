a=input().split()
b=input().split()
cnt=0
for i in a:
    if i in b:
        if a.count(i)==1 and b.count(i)==1:
            cnt+=1
print(cnt)