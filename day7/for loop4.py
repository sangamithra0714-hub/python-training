n=5
space=3
for i in range(1,n+1):
        if i==n or i==1:
            print("*"*n,end="")
            print()
        else:
            print("*"+space*" "+"*")
