import pandas as pd
import matplotlib.pyplot as plt


print("="*50)
print("CUSTOMER SEGMENT ANALYSIS")
print("="*50)


# Load segmented dataset

df = pd.read_csv("../Output/segmented_customers.csv")


print("\nSegmented Customer Data:")
print(df.head())


# Analyze each cluster

cluster_summary = df.groupby("Cluster").agg(
    {
        "Age": "mean",
        "AnnualIncome": "mean",
        "SpendingScore": "mean",
        "CustomerID": "count"
    }
)


cluster_summary.rename(
    columns={
        "CustomerID": "Customer_Count"
    },
    inplace=True
)


print("\nCluster Summary:")
print(cluster_summary)


# Save cluster summary

cluster_summary.to_csv("../Output/cluster_summary.csv")

print("\nCluster Summary Saved Successfully")


# Assign business names to clusters

cluster_names = {
    0: "Low Value Customers",
    1: "Premium Customers",
    2: "Average Customers",
    3: "High Spending Customers",
    4: "Budget Customers"
}


df["Segment"] = df["Cluster"].map(cluster_names)


print("\nCustomer Segments Added:")
print(df.head())


# Save final customer segments dataset

df.to_csv("../Output/final_customer_segments.csv", index=False)


print("\nFinal Customer Segment Dataset Saved Successfully")


# Visualization

plt.figure(figsize=(8,5))

plt.bar(
    cluster_summary.index,
    cluster_summary["SpendingScore"]
)

plt.title("Average Spending Score by Cluster")
plt.xlabel("Cluster")
plt.ylabel("Average Spending Score")

plt.show()


print("\nCustomer Segment Analysis Completed Successfully")