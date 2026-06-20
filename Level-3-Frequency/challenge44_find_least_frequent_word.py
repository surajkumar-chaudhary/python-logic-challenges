text = "apple banana apple mango banana apple"

min_count = None
least_frequent_word = None

freq = {}

words = text.split()

for word in words:
    freq[word] = freq.get(word, 0) + 1

for key, value in freq.items():
    if min_count is None or value < min_count:
        min_count = value
        least_frequent_word = key

print("Minimum count:", min_count)
print("Least frequent word:",least_frequent_word)
print(freq)