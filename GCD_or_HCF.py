a,b=map(int,input().split())
c=[]
for i in range(1,b//2+1):
    if b%i==0:
        c+=[i]
for i in c[::-1]:
    if a%i==0:
        gcd=i
        break
print(gcd)