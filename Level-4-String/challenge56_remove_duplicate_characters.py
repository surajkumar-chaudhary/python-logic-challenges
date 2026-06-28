text = "programming"

unique_char = []

for ch in text:
    if ch not in unique_char:
        unique_char.append(ch)

result = ''.join(unique_char)
print("result:", result)