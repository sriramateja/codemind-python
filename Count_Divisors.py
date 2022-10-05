a,b,c=map(int,input().split())
cn=0
for i in range(a,b+1):
    if i%c==0:
        cn+=1
print(cn)