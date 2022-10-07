a=input()
b=list(map(int,input().split()))
c=b[::-1]
for i in c:
    if i%2==0:
        print(i)
        break