arr = [2,1,-3,4]
largest_number = None
for num in arr:
    if largest_number is None or num > largest_number:
        largest_number = num

print(largest_number)