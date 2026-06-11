arr = [1,20, 4, 6,20, 8, -1, 2, 18,4]

largest_number = None
smallest_number = None

for num in arr:
    if largest_number is None or num > largest_number:
        largest_number = num
    if smallest_number is None or num < smallest_number:
        smallest_number = num

difference = largest_number - smallest_number
print("Difference is:", difference)