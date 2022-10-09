a=input()
c=0
cn1=1
b=list(map(int,input().split()))
for i in b:
    cn1+=1
    if cn1%2==0:
        c+=i
    else:pass
print(c)
    