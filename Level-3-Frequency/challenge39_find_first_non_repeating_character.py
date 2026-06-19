text = "character"

first_repeating_char = None

dis = {}

for n in text:
    dis[n] = dis.get(n,0) + 1

for ch in text:
    if dis[ch] > 1:
        first_repeating_char = ch
        break

print("First repeating character:", first_repeating_char)