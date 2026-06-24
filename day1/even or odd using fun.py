def evenorodd (a):
    if a%2==0:
        return "Even"
    else:
        return "Odd"
print(evenorodd(int(input("Enter a number: "))))
evenorodd=lambda a:"Even" if a%2==0 else "Odd"
print(evenorodd(int(input("Enter a number: "))))
