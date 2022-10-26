a=['a','e','i','o','u''A','E','I','O','U']
cnt=[]
fi=[]
b=list(input().split())
for i in b:
    for x in i:
        if x  in a :
            cnt+=[x]
print(len(cnt))
        