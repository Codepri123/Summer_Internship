# import pandas as pd
# data = {
#     "Joining_Date":["2026-06-20","2026-06-21","2026-06-22"]
# }
# df=pd.DataFrame(data)
# df["Date"]=pd.to_datetime(df["Joining_Date"])
# print(df)
import pandas as pd

df = pd.DataFrame({
    "Name": ["A", "B"],
    "Math": [80, 90],
    "Science": [85, 95]
})
df_melted = pd.melt(df, id_vars=["Name"], var_name="Subject", value_name="Marks")

print(df_melted)