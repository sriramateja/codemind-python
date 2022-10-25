a,b=map(int,input().split())
y=cnt=0
c=list(input().split())
for i in c:
    for x in i:
        if x.isdigit():
            y+=1
    if y==b:
        cnt+=1
        y=0
    else:y=0
print(cnt)
    