a=input()
b=input()
s=c=0
for i in range(int(a)):
    s=sum(list(map(int,input().split())))
    c+=s
print(c)