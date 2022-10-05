a=int(input())
b=[]
for i in range(1,a+1):
    i=str(i)
    b+=[i]
for x in range(a):
    c=a-x
    z=b[:c]
    s=''
    for y in z:
        s+=y
    print(s)
        

        