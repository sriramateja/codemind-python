cnt1=cnt2=0
for _ in range(int(input())):
    x=input()
    if '++' in x:
        cnt1+=1
    if '--' in x:
        cnt2+=1
print((cnt1-cnt2))
    