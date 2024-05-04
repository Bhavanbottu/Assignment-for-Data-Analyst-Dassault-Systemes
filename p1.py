import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the healthcare data
data = pd.read_csv("healthcare_dataset.csv")

# Plot correlation between Blood Group Type, Gender, and Medical Condition
cross_table = pd.crosstab(index=data['Blood Group Type'], columns=[data['Gender'], data['Medical Condition']])
plt.figure(figsize=(10, 6))
sns.heatmap(cross_table, annot=True, cmap="coolwarm", fmt='g')
plt.title('Correlation between Blood Group Type, Gender, and Medical Condition')
plt.xlabel('Gender, Medical Condition')
plt.ylabel('Blood Group Type')
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()



