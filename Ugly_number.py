a=int(input())
if a ==1:
    print('Ugly Number')
else:
    b=[]
    cnt2=0
    for i in range(2,a):
        cnt=0
        for j in range(2,i):
            if i%j==0:
                cnt+=1
        if cnt==0:
            if a%i==0:
                if i>6:
                    cnt2+=1
                b+=[i]
    if cnt2==0 and (len(b)!=0):
        print('Ugly Number')
    elif (cnt2>0) or len(b)==0:
        print('Not Ugly Number')