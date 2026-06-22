# # merge of lists
# list_1=[1,2,3,4,5]
# list_2=[7,8,9,10]
# print(list_1+list_2)
list_1 = [1, 2, 3, 4, 5]
list_2 = [7, 8, 9, 10]

merged = []

for i in list_1:
    merged.append(i)
for j in list_2:
     merged.append(j)
print(merged)