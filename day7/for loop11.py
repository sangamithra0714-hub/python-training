n=7
space=6
a=1
for i in range(1,n+1):
     print(space*" "+"*"*a+space*" ")
     space-=1
     a+=2
a=11
space=1
for j in range(1,n):
    print(space*" "+"*"*a+space*" ")
    space+=1
    a-=2
