import pandas as pd
df1 = pd.DataFrame({"ID":[1,2], "Name":["A","B"]})
df2 = pd.DataFrame({"ID":[3,4], "Name":["C","D"]})
x=pd.concat([df1,df2],axis=1)
print(x)


