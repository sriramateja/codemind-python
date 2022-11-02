a=input()
co=v=sp=d=0
li=['a','e','i','o','u','A','E','I','O','U']
for i in a:
    if i.isdigit():
        d+=1
    elif i in li:v+=1
    elif i not in li and i!=' ':co+=1
    elif i==' ':sp+=1
msg='Vowels: {}'.format(v)
print(msg)
msg='Consonants: {}'.format(co)
print(msg)
msg='Digits: {}'.format(d)
print(msg)
msg='White spaces: {}'.format(sp)
print(msg)