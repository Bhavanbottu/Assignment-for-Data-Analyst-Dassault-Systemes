# Task 1b: Find average billing amount for each medical condition
import pandas as pd

# Load the healthcare data
data = pd.read_csv("healthcare_dataset.csv")

# Find average billing amount for each medical condition
avg_billing = data.groupby('Medical Condition')['Billing Amount'].mean()
print("Average Billing Amount for Each Medical Condition:")
print(avg_billing)