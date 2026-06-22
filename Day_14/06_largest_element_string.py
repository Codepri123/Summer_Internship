#largest element in the string
lst = [1, 2, 3, 4, 5]

largest = lst[0]

for num in lst:
    if num > largest:
        largest = num

print("Largest element:", largest)