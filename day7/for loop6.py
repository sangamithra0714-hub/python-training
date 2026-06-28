n=4
a=5
space=1
for i in range(7,1,-1):
    for j in range(1):
        if i==7:
            print("*"*i,end="")
            print()
        else:
            print(space*" "+a*"*"+space*" ")
            space+=1
            a-=2
n=4  
a=7
space=0
for i in range(n):
    print(space*" "+a*"*"+space*" ")
    space=space+1
    a=a-2
