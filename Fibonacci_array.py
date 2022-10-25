def isfib(z,a):
    for i in range(2,a):
        be=z[i-1]
        pr=z[i-2]
        cu=z[i]
        if cu!=pr+be:return False
    return True
a=int(input())
if a<=2:print('no')
else:
    x=list(map(int,input().split()))
    b=isfib(x,a)
    if b:print('yes')
    else:print('no')