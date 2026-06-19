text = "characteraaa"

duplicate_char = []

freq = {}

for ch in text:
    freq[ch] = freq.get(ch,0) + 1
    
for ch, count in freq.items():
    if count > 1:
        duplicate_char.append(ch)
print(duplicate_char)