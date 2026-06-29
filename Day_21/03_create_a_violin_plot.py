import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
df=sns.load_dataset("tips")
print(df)
sns.violinplot(df,x="day",y="tip",hue="sex")
plt.show()