arr = [2,1,-3,4]

smallest_number = arr[0]

for num in arr:
    if num < smallest_number:
        smallest_number = num
        
print(smallest_number)