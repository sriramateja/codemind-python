cn1=cn2=cn3=0
a,b,c=map(int,input().split())
if a>50:cn1=1
if b>60:cn2=1
if c>100:cn3=1
s=cn1+cn2+cn3
if s==3:
    print(10)
elif s==0:
    print(5)
elif cn1+cn2==2:
    print(9)
elif cn2+cn3==2:
    print(8)
elif cn1+cn3==2:
    print(7)
elif s==1:print(6)