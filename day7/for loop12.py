n=5
space=4
b=1
for i in range(1,n+1):
    if 2<=i and i<n:
        space-=1
        print(space*" "+"*"+" "*b+"*"*1+space*" ")
        b+=2
    elif i==1:
        print(space*" "+"*"*i+space*" ")
    else:
        print("*"*(2*n-1))
            
