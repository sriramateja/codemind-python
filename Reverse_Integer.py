a=input()
if a[0]=='+' or a[0]=='-':
    c=a[0]
    b=a[::-1]
    e=c+b
    f=len(e)-1
    print(int(e[:f]))
else:print(int(a[::-1]))

        
        