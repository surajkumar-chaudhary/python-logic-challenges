text = "apple banana apple mango banana apple"

words = text.split()

freq = {}
maximum_count = None
most_frequent_word = None

for word in words:
    freq[word] = freq.get(word, 0 ) + 1

for key,value in freq.items():
    if maximum_count is None or value > maximum_count:
        maximum_count = value
        most_frequent_word = key

print("Maximum count:",maximum_count)
print("Most frequent word:",key)