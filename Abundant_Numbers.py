a=int(input())
b=0
for i in range(1,(a//2)+1):
    if a%i==0:
        if i%2 or i%3 or i%4 or i%5 ==0:
            b+=i
        else:pass
if b>a:print('True')
else:print('False')
        
    