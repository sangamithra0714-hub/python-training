a="a"
b=ord(a)
if b>=65 and b<=90:
  print("Uppercase")
elif b>=97 and b<=122:
   print("Lowercase")
elif b>=48 and b<=56:
   print("Digits")
else:
    print("Special character")
    
a=65
b=chr(a)
if b>= 'A' and b<= 'Z':
   print("Uppercase")
elif b>= 'a' and b<= 'z':
    print("Lowercase")
elif b>= '0' and b<= '9':
    print("Digits")
else:
    print("Special character")
