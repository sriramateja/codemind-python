a=input()
b=int(a[::-1])
c=b**2
d=int(a)
e=str(d**2)
if e[::-1]==str(c):print('True')
else:print('False')