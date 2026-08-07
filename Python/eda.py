import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("="*50)
print("CUSTOMER SEGMENTATION - EDA")
print("="*50)

# Load cleaned dataset
df = pd.read_csv("../Output/cleaned_customers.csv")

print("\nFirst 5 Records:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())


# Gender Distribution
plt.figure(figsize=(6,4))
sns.countplot(data=df, x="Gender")
plt.title("Customer Distribution by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Customers")
plt.show()


# Age Distribution
plt.figure(figsize=(7,4))
sns.histplot(df["Age"], bins=10, kde=True)
plt.title("Age Distribution of Customers")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()


# Annual Income Distribution
plt.figure(figsize=(7,4))
sns.histplot(df["AnnualIncome"], bins=10, kde=True)
plt.title("Annual Income Distribution")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Count")
plt.show()


# Spending Score Distribution
plt.figure(figsize=(7,4))
sns.histplot(df["SpendingScore"], bins=10, kde=True)
plt.title("Spending Score Distribution")
plt.xlabel("Spending Score")
plt.ylabel("Count")
plt.show()


# Income vs Spending Score
plt.figure(figsize=(7,5))
sns.scatterplot(
    data=df,
    x="AnnualIncome",
    y="SpendingScore",
    hue="Gender",
    s=100
)

plt.title("Annual Income vs Spending Score")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score")
plt.show()


print("\nEDA Completed Successfully")