import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
df=sns.load_dataset("flights")
print(df)
sns.countplot(df,x="passengers")
plt.show()