#move all zeroes to end 
list=[0,2,0,0,5,6]
    
for i in range(len(list)):
    for j in range(len(list) - 1 - i):
        if list[j] == 0:
            list[j], list[j + 1] = list[j + 1], list[j]
    else:
        pass
print(list)    

