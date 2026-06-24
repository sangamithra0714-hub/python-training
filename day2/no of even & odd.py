a=int(input())
even=0
odd=0
for i in range(1,a+1):
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
print(even)
print(odd)
