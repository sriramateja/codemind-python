a=input().split()
b=[]
for i in a:
    b+=[min(i)]
    b+=[max(i)]
print(*b)