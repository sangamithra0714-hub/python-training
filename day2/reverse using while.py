a=int(input())
rev=0
while a>0:
    last=a%10
    a=a//10
    rev=(rev*10)+last
print(rev)
