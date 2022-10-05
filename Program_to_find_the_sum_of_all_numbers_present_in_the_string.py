a=input()
b=0
for i in a:
    if i.isdigit():
        i=int(i)
        b+=i
print(b)