# arr = [34,34,1, 4, 6,20, -8, -1, 2, 18, 20,20,20,32,32,34]
arr = [34,34,1,4,6,20,32,32,34]
highest_number = None
second_highest_number = None
highest_number_count = 0

for index,num in enumerate(arr):
    if highest_number is None or num > highest_number:
        second_highest_number = highest_number
        highest_number = num
        highest_number_count = 1
    elif num == highest_number:
        highest_number_count += 1
    elif num < highest_number:
        if second_highest_number is None or num > second_highest_number:
            second_highest_number = num
print("Largest number:", highest_number)
print("Count of largest number:",highest_number_count)
print("Second largest number:", second_highest_number)