arr = [1,5,4,3,2,1]

largest_number = None
second_largest_number = None
third_largest_number = None

for num in arr:
    if largest_number is None or num > largest_number:
        third_largest_number = second_largest_number
        second_largest_number = largest_number
        largest_number = num
    elif second_largest_number is None or num > second_largest_number:
        third_largest_number = second_largest_number
        second_largest_number = num
    elif third_largest_number is None or num > third_largest_number:
        third_largest_number = num
        

print("Third largest number:",third_largest_number)
print("Second largest number:",second_largest_number)
print("Largest number:",largest_number)


