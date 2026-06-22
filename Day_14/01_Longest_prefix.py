string=["apple","appngo", "appvacdo"]
prefix=string[0]
for i in string[1:]:
    while not i.startswith(prefix):
        prefix=prefix[:-1]
print(prefix)        

