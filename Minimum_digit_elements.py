a=input()
cnt=0
b=list(map(int,input().split()))
c=len(str(min(b)))
for i in b:
    i=str(i)
    if len(i)==c:cnt+=1
print(cnt)
