n=4
a=n*(n+1)//2
for i in range(n,0,-1):
    for j in range(i):
        print(a,end="")
        a-=1
    print()
