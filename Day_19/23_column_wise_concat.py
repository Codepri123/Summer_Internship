import pandas as pd
df1 = pd.DataFrame({"Name":["A","B"]})
df2 = pd.DataFrame({"Age":[20,21]})
x=pd.concat([df1,df2],axis=0)
print(x)

