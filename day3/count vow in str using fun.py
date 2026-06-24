def countvow(a):
    count=0
    s=['a','e','i','o','u']
    for ch in a:
        if ch in s:
            count=count+1
    return count
print(countvow("sangamithra"))
