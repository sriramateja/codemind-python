a=input().split()
b=a[-1]
mi=min(b)
if mi.isupper():
        ma=mi.lower()
        if ma in b:
            mi=ma
print(mi)