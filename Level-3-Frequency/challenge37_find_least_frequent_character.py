text = "apple banana apple mango banana apple cherry"

words = text.split()

dis = {}

least_frequent_char = None

count = None    

for word in words:
    dis[word] = dis.get(word, 0) + 1

for key, value in dis.items():
    if count is None or value < count:
        count = value
        least_frequent_char = key

print("Least frequent character:",least_frequent_char)
print("Count:",count)
        