text = "abc123@#$"

count = 0

for ch in text:
    if not ch.isalpha() and not ch.isdigit():
        count+= 1

print("Special Characters:",count)