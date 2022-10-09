a=input()
c=0
c2=0
cn1=1
b=list(map(int,input().split()))
for i in b:
    cn1+=1
    if cn1%2==0:
        c2+=i
    else:c+=i
print(c2-c)
    