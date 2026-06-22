#create a list of vowels from a string 
string=" hello "
visited=[]
for i in string:
    if i in  "Aeiouaieou" :
        visited.append(i)
    else:
        pass
print(visited)    