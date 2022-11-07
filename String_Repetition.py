a=input()
b=int(input())
x1=a.count('a')
c=b//len(a)
d=b%len(a)
o1=c*x1
if d==0:
    pass
else:
    for i in range(d):
        x2=a[i]
        if x2=='a':o1+=1
print(o1)
