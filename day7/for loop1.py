n=5
space=4
for i in range(1,n+1):
    print(space*" ",end="")
    for j in range(i):
        print(i,end="")
    print()
    space-=1
