import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset("tips")

print(df)

# Heatmap
sns.heatmap(
    df.corr(numeric_only=True),
    cmap="Blues",
    annot=True
)

plt.show()