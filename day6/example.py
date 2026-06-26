f = open("data.txt", "r")
text = f.read().lower()
print("Text:", text)

count = 0

for ch in text:
    if ch in "aeiou":
        count += 1

print("Number of vowels:", count)

f.close()
