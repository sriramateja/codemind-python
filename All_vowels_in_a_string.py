a=['a','e','i','o','u']
d=['A','E','I','O','U']
cnt=[]
fi=[]
b=list(input().split())
for i in b:
    for x in i:
        if x  in a and x not in cnt:
            cnt+=[x]
        else:
            if x in d and x not in fi:
                fi+=[x]
if len(cnt)==5 or len(fi)==5:print('True')
else:print('False')