a=list(input())
b=[]
for i in a:
    b+=[ord(i)]
print(chr(max(b)))
