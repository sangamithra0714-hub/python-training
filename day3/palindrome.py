def palindrome(x): 
    if x<0:
        print(x, "is not a palindrome")
    elif x>0:
        s=x
        rev = 0
        while x > 0:
            last = x % 10
            x = x // 10
            rev = (rev * 10) + last
        if s==rev:
            print(s, "is a palindrome")
        else:
            print(s, "is not a palindrome")
palindrome(int(input("Enter a number: ")))

