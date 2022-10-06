a,b=map(int,input().split())
x=[]
for i in range(1,a+1):
    if a%i==0:
        x+=[i]
c=x[::-1]
for i in c:
    if b%i==0:
        print(i)
        break