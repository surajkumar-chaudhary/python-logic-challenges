arr = [12, -7, 4, -15, 9, -2, 18, -5]

last_positive_number = None
second_last_positive_number = None
third_last_positive_number = None

for num in arr:
    if num>0:
        third_last_positive_number = second_last_positive_number
        second_last_positive_number = last_positive_number
        last_positive_number = num

print(third_last_positive_number)