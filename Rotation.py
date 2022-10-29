for _ in range(int(input())):
    a,b=map(int,input().split())
    arr=list(map(int,input().split()))
    if b>a:b=b%a
    x=(arr[:-b])
    y=arr[-b:]
    print(*y+x)
    