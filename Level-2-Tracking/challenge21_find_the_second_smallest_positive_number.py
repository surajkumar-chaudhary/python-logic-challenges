arr = [1,20, 4, 6, -8, -1, 2, 1,-4]

first_smallest_number = None

second_smallest_positive_number = None

for num in arr:
    if num>0:
        if first_smallest_number is None or num < first_smallest_number:
            second_smallest_number = first_smallest_number
            first_smallest_number = num
        elif first_smallest_number < num:
            if second_smallest_number is None or second_smallest_number > num:
                second_smallest_number = num

print(second_smallest_number)
print(first_smallest_number)