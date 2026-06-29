text = "programming"

no_vowels = []

for ch in text:
    if ch not in 'aeiou':
        no_vowels.append(ch)

result = ''.join(no_vowels)

print(result)