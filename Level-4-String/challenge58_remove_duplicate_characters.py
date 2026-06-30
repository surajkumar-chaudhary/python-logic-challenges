text = "I love Python"

result = ""
for ch in text:
    if ch == " ":
        result += "-"
    else:
        result += ch
print(result)