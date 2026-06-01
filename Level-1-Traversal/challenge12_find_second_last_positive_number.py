arr = [12, -7, 4, -15, 9, -2, 18, -5]

second_last_positive_number = None
last_positive_number = None

for num in arr:
    if num>0:
        second_last_positive_number = last_positive_number
        last_positive_number = num
    
print(second_last_positive_number)