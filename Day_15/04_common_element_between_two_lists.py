#Find common elements between two lists.
list_1=[1,2,3,4,5,6]
list_2=[6,7,8,9,10]
list_3=[]
for i in list_1:
    for j in list_2:
        if i==j:
            list_3.append(i)
        else:
            pass
print(list_3)        
    

