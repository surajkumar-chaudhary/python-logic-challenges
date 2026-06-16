arr = [10,1,-5,4,3,2,1]

largest_positive = None

for n in arr:
    if n>0:
        if largest_positive is None or n > largest_positive:
            largest_positive = n

print(largest_positive)