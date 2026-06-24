numbers = [1, 2, 3, 2, 1, 4, 2]

count = {}

for i in numbers:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
