import pandas as pd

df = pd.read_csv("../Dataset/customers.csv")

print(df.head())

print(df.info())

print(df.isnull().sum())

df.to_csv("../Dataset/cleaned_customers.csv", index=False)

print("Completed Successfully")
import os

# Create Output folder if not exists
os.makedirs("../Output", exist_ok=True)

# Save cleaned dataset
df.to_csv("../Output/cleaned_customers.csv", index=False)

print("Cleaned Dataset Saved Successfully")