text = "apple banana apple mango banana apple"

words = text.split()

dis = {}

most_frequent_char = None
max_value = None
for word in words:
    dis[word] = dis.get(word,0) + 1

for key,value in dis.items():
    if max_value is None or value > max_value:
         max_value = value
         most_frequent_char = key


print("Most frequent character :",most_frequent_char)
print("count:", max_value)