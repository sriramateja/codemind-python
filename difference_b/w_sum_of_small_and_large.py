b=input().split()
mi=ma=0
for a in b:
    ma+=ord(max(a))
    mi+=ord(min(a))
print(ma-mi)