arr = [-7, -15, 9, -2, 18, -5]

first_positive_number = 0

for num in arr:
    if num>0:
        first_positive_number = num
        break

print(first_positive_number)