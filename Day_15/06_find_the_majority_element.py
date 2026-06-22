#majority element in the list
n=[1,2,3,4,5,5,5,5,5]
total=len(n)//2
print(total)
freq={}
for i in n:
    if i in  freq:
     freq[i]+=1
    else:
     freq[i]=1
print(freq)    
for key in freq:
    if freq[key] >= total:
        print("Majority element:", key)

    else: 
     pass