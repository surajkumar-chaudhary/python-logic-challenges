text = "characteraa"

vowel_count = 0
consonant_count = 0

for ch in text:
    if ch.isalpha() and ch not in 'aeiou':
            consonant_count += 1
# for ch in text:
#     if ch.isalpha():
#         if ch not in 'aeiou':
#             consonant_count += 1
#         else:
#             vowel_count += 1

# print(vowel_count)
print(consonant_count)