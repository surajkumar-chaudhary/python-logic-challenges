word_one = 'tea'
word_two = 'eat'



if sorted(word_one) == sorted(word_two):
    print("Anagram")
else:
    print("Not anagram")

# words = ['eat', 'tea' , 'rat' , 'cat' , 'ate' ]

# dis = {}

# for word in words:
#     sort = sorted(word)
#     join = ''.join(sort)
#     if join in dis:
#         dis[join].append(word)
#     else:
#         dis[join] = [word]

# print(sort)
# print(join)
# print(dis)