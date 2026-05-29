arr = [-1, 3, 4, -2, 0]

minimum = None

for num in arr:
    if num > 0:
        if minimum is None or num < minimum:
            minimum = num

print(minimum)