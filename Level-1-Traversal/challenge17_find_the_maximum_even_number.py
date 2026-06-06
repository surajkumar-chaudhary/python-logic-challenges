arr = [12, 5, 4, 15, 9, 10, 18]

max_even_number = None

for num in arr:
    if num>0:
        if num%2==0:
            if max_even_number is None or num > max_even_number:
                max_even_number = num

print(max_even_number)