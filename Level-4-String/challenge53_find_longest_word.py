text = "I love programming in Python programming sefrdcvbgra"

words = text.split()

max_length = 0
longest_word = None
multiple = []

for word in words:
    if len(word) > max_length:
        max_length = len(word)
        multiple = [word]
    
    elif len(word)  == max_length:
        multiple.append(word)
    

print("Maximum length:", max_length)
print("Longest word:", multiple)

