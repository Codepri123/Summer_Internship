arr = [100, 4, 200, 1, 3, 2]

# Bubble Sort
n = len(arr)


y= sorted(arr)
print(y)

longest = 1
current = 1

for i in range(1, n):
    if y[i] == y[i - 1] + 1:
        current += 1
    else:
        if current > longest:
            longest = current
        current = 1

if current > longest:
    longest = current
print(" Length of Longest Consecutive Sequence:", longest)
