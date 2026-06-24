def primeornot(a):
    if a <= 1:
        print("not prime")
        return

    for i in range(2, a):
        if a % i == 0:
            print("not prime")
            return
    print("prime")
primeornot(int(input("Enter a number: ")))
