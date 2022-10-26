b=input().split()
c=[]
for a in b:
    c+=[(ord(max(a))-ord(min(a)))]
print(*c)