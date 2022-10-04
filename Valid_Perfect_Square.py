import math
for _ in range(int(input())):
    b=int(input())
    c=int(math.sqrt(b))
    if c*c==b:print('True')
    else:print('False')