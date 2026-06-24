def function(a):
    if a%3==0 and a%8==0:
        print(a, "is divisible by 3 and 8")
    else:
        print(a, "is not divisible by 3 and 8")
function(int(input("Enter a number: ")))
