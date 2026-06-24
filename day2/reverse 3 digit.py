a="123"
print(a[-1], a[-2], a[-3])
n=1234
o=1234%10
n=n//10
t=n%10
n=n//10
h=n%10
n=n//10
e=n%10
c=o*1000+t*100+h*10+e
print(c)

a=1234
b=0
while a>0:
    last=a%10
    b=b*10+last
    a=a//10
print(b)
