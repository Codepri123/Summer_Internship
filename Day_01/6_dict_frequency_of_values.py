data=[1,2,3,1,2,2,3,4]
data_1={}
for i in data:
    if i not in data_1:
        data_1[i]=1
    else:
        data_1[i]+=1
print(data_1)        
