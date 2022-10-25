a=input()
z=[]
y=0
c=list(input().split())
for i in c:
    for x in i:
        if x.isdigit():
            y+=1
    z+=[y]
    y=0
print(*z)
    