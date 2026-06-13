arr = [34,34,1,4,6,20,1,1,-1,32,32,34]

smallest_number = None

count = 0

for num in arr:
    if smallest_number is None or num < smallest_number:
        smallest_number = num
        count = 1
    elif num == smallest_number:
        count += 1

print("Smallest number is:", smallest_number)
print("Smallest number count is:", count)

# players = {
#     "Ram": 85,
#     "Hari": 92,
#     "Sita": 95,
#     "Gita": 95,
#     "Shyam": 95
# }

# h_score = None
# top_players = []
# for player , score in players.items():
#     if h_score is None or score > h_score:
#         h_score = score
#         top_players = [player]
#     elif h_score == score:
#         top_players.append(player)
# print("Top players:",", ".join(top_players))
# print(h_score)