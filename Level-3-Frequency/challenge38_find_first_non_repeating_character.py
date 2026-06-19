text = "character"

first_non_repeating_char = None

dis = {}
for n in text:
    dis[n] = dis.get(n,0) + 1
for ch in text:
    if dis[ch] == 1:
        first_non_repeating_char = ch
        break
print(first_non_repeating_char)
