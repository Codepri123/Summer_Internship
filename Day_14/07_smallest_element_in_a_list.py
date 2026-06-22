#find the smallest element in the list /8
lst = [1, 2, 3, 4, 5]

smallest = lst[0]

for num in lst:
    if num < smallest:
        smallest = num

print("smallest element:", smallest)