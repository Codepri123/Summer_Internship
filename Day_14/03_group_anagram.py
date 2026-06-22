words=["eat","tea","tan","ate","nat","bat"]
group=[]
for i in words:
    found=False
    for j in group:
        if sorted(i)==sorted(group):
            group.append(words)
            found =True
            break
    if not found:
      group.append([i])
print(group)

