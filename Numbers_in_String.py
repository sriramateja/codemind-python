a=input()
sum=0
for i in a:
    if i.isdigit():
        i=int(i)
        sum+=i
print(sum)