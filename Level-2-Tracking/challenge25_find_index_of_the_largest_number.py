arr = [1, 4, 6,20, -8, -1, 2, 18, 20]

largest_number = None
# index_number = []
# largest = max(arr)
for index,num in enumerate(arr):
    if largest_number is None or num > largest_number:
        largest_number = num
        index_number = index 

print(index_number)
# for index, num in enumerate(arr):
#     if num == largest:
#         index_number.append(index)



