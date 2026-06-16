arr = [1 ,-5 ,4 ,4 ,30 ,2 ,-7]

first_largest = None
second_largest_distinct_number = None

for n in arr:
    if n>0:
        if first_largest is None or n > first_largest:
            second_largest_distinct_number = first_largest
            first_largest = n
        elif first_largest!=n and (
            second_largest_distinct_number is None or n > second_largest_distinct_number):
            second_largest_distinct_number= n
        
print("Second Largest distinct number is:",second_largest_distinct_number)