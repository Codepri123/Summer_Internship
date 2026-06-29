import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
df=sns.load_dataset("tips")
print(df)
sns.stripplot(df,x="day",y="tip",jitter=True)
plt.bar(df["day"],
         df["tip"])
plt.show()