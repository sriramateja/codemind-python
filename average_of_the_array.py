a=int(input())
b=list(map(int,input().split()))
c=sum(b)/a
msg='{:.2f}'.format(c)
print(msg)
    