a,c=input().split()
su=su1=0
for i in range(int(a)):
    b=list(map(int,input().split()))
    for x in b:
        if x%2==0:
            su+=x
        else:
            su1+=x
print(su,su1)