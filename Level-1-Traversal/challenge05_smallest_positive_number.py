arr = [12, -7, 4, -15, 9, -2, 18, -5]

smallest_positive_number = None

for num in arr:
    if num>0:
        if smallest_positive_number is None or num < smallest_positive_number:
            smallest_positive_number = num

print(smallest_positive_number)