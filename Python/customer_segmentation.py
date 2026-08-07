import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


print("="*50)
print("CUSTOMER SEGMENTATION USING K-MEANS")
print("="*50)


# Load cleaned data
df = pd.read_csv("../Output/cleaned_customers.csv")


print("\nDataset Loaded Successfully")
print(df.head())


# Select features for clustering
X = df[["AnnualIncome", "SpendingScore"]]


# Feature Scaling
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)


print("\nData Scaling Completed")


# Finding optimal clusters using Elbow Method

wcss = []

for i in range(1, 11):
    kmeans = KMeans(
        n_clusters=i,
        random_state=42,
        n_init=10
    )

    kmeans.fit(X_scaled)

    wcss.append(kmeans.inertia_)


plt.figure(figsize=(7,4))

plt.plot(range(1,11), wcss, marker="o")

plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")

plt.show()


print("\nElbow Method Completed")
# Applying K-Means with optimal clusters

optimal_clusters = 5

kmeans = KMeans(
    n_clusters=optimal_clusters,
    random_state=42,
    n_init=10
)


# Create clusters
df["Cluster"] = kmeans.fit_predict(X_scaled)


print("\nCustomer Segmentation Completed")

print("\nCluster Distribution:")
print(df["Cluster"].value_counts())


# Save segmented data

df.to_csv("../Output/segmented_customers.csv", index=False)

print("\nSegmented Dataset Saved Successfully")


# Visualize Customer Segments

plt.figure(figsize=(8,5))

plt.scatter(
    df["AnnualIncome"],
    df["SpendingScore"],
    c=df["Cluster"],
    s=100
)

plt.title("Customer Segmentation")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score")

plt.show()