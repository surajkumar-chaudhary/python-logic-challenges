arr = [1,20, 4, 6,20, -8, -1, 2, 18,-4]

first_largest_number = None
second_largest_number = None

for num in arr:
    if first_largest_number is None or num > first_largest_number:
        second_largest_number = first_largest_number
        first_largest_number = num
    elif first_largest_number > num:
        if second_largest_number is None or num > second_largest_number:
            second_largest_number = num

print("The two largest numbers are:", second_largest_number,first_largest_number)