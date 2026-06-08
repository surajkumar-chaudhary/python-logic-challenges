arr = [20, 30, 10, 25]

largest_number = None
second_largest_number = None

for num in arr:
    if largest_number is None or num > largest_number:
        second_largest_number = largest_number
        largest_number = num
    elif largest_number > num:
        if second_largest_number is None or second_largest_number < num:
            second_largest_number = num 

print(second_largest_number)
print(largest_number)