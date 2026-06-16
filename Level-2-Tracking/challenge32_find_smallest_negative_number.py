arr = [10,1,-5,4,3,2,-7]

largest_negative = None

for n in arr:
    if n<0:
        if largest_negative is None or n < largest_negative:
            largest_negative = n

print(largest_negative)