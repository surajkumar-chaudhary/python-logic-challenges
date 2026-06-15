arr = [1,5,4,3,2,1]

smallest = None
second_smallest = None
third_smallest = None

for num in arr:
    if smallest is None or num < smallest:
        third_smallest = second_smallest
        second_smallest = smallest
        smallest = num
    elif second_smallest is None or (
        num < second_smallest and smallest != num):
        third_smallest = second_smallest
        second_smallest = num
    elif third_smallest is None or (
        num < third_smallest and smallest != num and second_smallest != num):
        third_smallest = num

print(third_smallest)
print(second_smallest)
print(smallest)