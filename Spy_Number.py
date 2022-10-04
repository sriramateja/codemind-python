a=input()
b=1
c=0
for i in a:
    i=int(i)
    b*=i
    c+=i
if b==c:print('Spy Number')
else:print('Not Spy Number')