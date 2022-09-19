a=input()
b=0
for i in a:
    ind=a.index(i)
    ind=int(ind)
    ind2=ind+1
    i=int(i)
    z=i**ind2
    b+=z
if b==int(a):print('True')
else:print('False')