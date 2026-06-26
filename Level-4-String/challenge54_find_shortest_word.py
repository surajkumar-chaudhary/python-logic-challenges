text = "I love in Python programming"

words = text.split()
multiple_shortest_word = []
length = None

for word in words:
    if length is None or len(word) < length:
        length  = len(word)
        multiple_shortest_word = [word]
    elif length == len(word):
        multiple_shortest_word.append(word)

print("Shortest words:", multiple_shortest_word)
print("Lnegth of the word:", length)