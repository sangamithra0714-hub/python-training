try:
    a=int(input("Enter value of a:"))
    d=10/a
    print(d)
except ValueError as v:
    print("a should be integer not a string or character:",v)
except ZeroDivisionError as z:
    print("divide by 0 gives infinity,so pls enter some other value:",z)
finally:
    print("program is done")
