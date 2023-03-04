t=int(input())
while(t>0):
	
    n=int(input())
    x=0
    a=list(map(int, input().split()))
    for i in a:
        x+=a
    y=x/n
    z=x%n
    a.sort()
    j=0
    i=n-1
    while(i>n-1-z):
	    
	    j+=abs(a[i]-y-1)
while(i>=0):
	    
    j+=abs(a[i]-y)
    i-=1
	    
    j/=2
    print(j)
    t-=1
