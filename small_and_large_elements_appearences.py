def cnt(a,so):
    cnt=0
    for z in a:
        for rm in z:
            if rm==so:cnt+=1
    return cnt
a=input().split()
ss=[]
mi='z'
ma='a'
for i in a:
    xa=min(i)
    if xa<mi:
        mi=xa
    xb=max(i)
    if xb>ma:
        ma=xb
ss+=[mi]
cn=cnt(a,mi)
ss+=[cn]
ss+=[ma]
cn=cnt(a,ma)
ss+=[cn]
print(*ss)
    