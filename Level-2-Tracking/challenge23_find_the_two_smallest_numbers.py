arr = [1,20, 4, 6,20, -8, -1, 2, 18,-4]

first_smallest_number = None
second_smallest_number = None

for num in arr:
    if first_smallest_number is None or num < first_smallest_number:
        second_smallest_number = first_smallest_number
        first_smallest_number = num
    elif num>first_smallest_number:
        if second_smallest_number is None or num < second_smallest_number:
            second_smallest_number = num

print("The two smallest numbers are:", second_smallest_number,first_smallest_number)