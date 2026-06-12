arr = [1, 4, 6,20, -8, -1, 2, 18, 20]

smallest_number = None
index_number = None

for index,num in enumerate(arr):
    if smallest_number is None or num < smallest_number:
        smallest_number = num
        index_number = index 

print(index_number)