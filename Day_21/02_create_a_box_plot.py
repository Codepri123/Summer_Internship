import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
df=sns.load_dataset("tips")
print(df)
sns.boxplot(df,x="day",y="total_bill",hue="smoker")
plt.show()