a=input()
c='x'
for i in a:
    if a.count(i)==1:
        c=a.index(i)
        break
if c=='x':print(-1)
else:print(c)