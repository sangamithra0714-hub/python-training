n=6
space=n-1
for i in range(1,n+1):
    print(space*" "+"*"*i)
    space-=1
space=1
for j in range(n-1,0,-1):
    print(space*" "+"*"*j)
    space+=1
