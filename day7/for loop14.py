n=6
space=5
b=1
for i in range(1,n+1):
    if i==1:
        print(space*" "+"*")
    else:
        space-=1
        print(space*" "+"*"+" "*b+"*"*1)
        b+=2

       
space=1
b=7
for j in range(n-1,0,-1):
    if j==1:
        print(space*" "+"*")
    else:
        print(space*" "+"*"+" "*b+"*")
    space+=1
    b-=2  
