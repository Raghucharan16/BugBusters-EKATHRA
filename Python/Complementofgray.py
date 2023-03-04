import random
t=int(input())
#print(t)
while(t):
    t-=1
    a=input()
    b=[]
    l=len(a)
    x=int(a[0])
    b.append(x)
    for i in range(1,l):
        y=int(a[i])
        z=y^x
        x=y
        b.append(z)
    for i in range(l):
        if(b[i]==1):
            b[i]=0
        else:
            b[i]=1
    i=l-1
    while(i>=0):
        if(b[i]==0):
            b[i]=l
            break
        else:
            b[i]=0
        i-=1
    if (i == -1):
        print('1',end='')
    for i in range(l):
        print(b[i],end='')
    print()
