a=input()
c=[]
d=''
e=['a','e','i','o','u','A','E','I','O','U']
for x in a:
    if x in e:
        b=a.index(x)
        d=x+d
        c+=[b]
su=''
cnt=-1
for z in a:
    f=a.index(z)
    if f in c:
        cnt+=1
        su=su+d[cnt]
    else:su+=z
print(su)
        