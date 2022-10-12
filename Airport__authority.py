b=[]
cnt=0
for x in range(int(input())):
    b+=[int(input())]
c=int(input())
for i in b:
    if i>c:
        cnt+=1
print(len(b)+cnt)
    
