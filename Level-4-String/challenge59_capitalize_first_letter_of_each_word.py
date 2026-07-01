text = "i love python programming"

words = text.split()
result = []

for word in words:
    
    fin = word[0].upper()
    res = fin + word[1:]
    result.append(res)

print(' '.join(result))