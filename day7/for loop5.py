n=7
t=n//2
b=n-t
for i in range(1,n+1):
    if i<=t:
        print("*"*i)
    else:
        print("*"*b)  
        b=b-1 
