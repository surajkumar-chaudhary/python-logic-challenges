arr = [12, -7, 4, -15, 9, -2, 18, -5]

largest_negative_number = None
for num in arr:
    if num<0:
        if largest_negative_number is None or num> largest_negative_number:
            largest_negative_number = num

print(largest_negative_number)
