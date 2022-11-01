import math
a,b,c=map(int,input().split())
s=(a+b+c)/2
s=s*(s-a)*(s-b)*(s-c)
s=math.sqrt(s)
msg='{:.2f}'.format(s)
print(msg)
