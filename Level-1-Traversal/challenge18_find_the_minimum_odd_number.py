arr = [12, 5, 3, 15, 9, -10, 1]

min_odd_number = None

for num in arr:
    if num>0:
        if num %2 != 0:
            if min_odd_number is None or num < min_odd_number:
                min_odd_number = num
print(min_odd_number)
