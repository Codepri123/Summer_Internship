import pandas as pd
var=pd.read_csv("C:\\Users\\User\\Downloads\\CustomerLoyaltyProgram.csv")
# print(var.head())
# print(var[var.duplicated()])
# print(var.tail())
# print(var.fillna("all"))
# print(var.fillna("python",inplace=True,limit=2))
# print(var.fillna(method="bfill"))
print(var.dropna(how="any"))