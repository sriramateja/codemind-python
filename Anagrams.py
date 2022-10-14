def isanag(x,y):
    for z in y:
        if z not in x:
            return False
            break
    return True
            
a=input().upper()
b=input().upper()
if isanag(a,b):
    print(True)
else:print(False)