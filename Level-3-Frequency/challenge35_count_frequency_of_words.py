text = "apple banana apple mango banana apple"

words = text.split()
dis= {}

for word in words:
    dis[word] = dis.get(word, 0) + 1

print(dis)