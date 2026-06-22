#flatten nested tuple
tuple= ((1, 2), (3, 4), (5, 6))
t=[]
for i in tuple:
    for j in i :
      t.append(j)
print(t)        