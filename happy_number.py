def happy(num):
    num=str(num)
    x=0
    for i in num:
        i=int(i)
        x+=i**2
    return x
a=int(input())
while a>9:
    a=happy(a)
if a==1 or a==9:
    print(True)
else:print(False)
    

        