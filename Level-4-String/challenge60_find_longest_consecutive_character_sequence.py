text = "aaabbbbccdddddee"

current_count = None
current_char = 0

longest_char = None
max_count = 0

for ch in text:
    if current_char == ch:
        current_count += 1
        if current_count>max_count:
            longest_char = ch
            max_count = current_count     
    else:
        current_char = ch
        current_count = 1

   

print(longest_char)
print(max_count)