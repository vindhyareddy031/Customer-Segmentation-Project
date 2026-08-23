# 📊 Customer Segmentation Using K-Means Clustering

## 📌 Project Overview

Customer Segmentation is a Machine Learning project that groups customers into different segments based on their **Annual Income** and **Spending Score**.

The project uses the **K-Means Clustering algorithm** to identify customers with similar purchasing behavior. These segments can help businesses understand their customers and develop targeted marketing strategies.

---

## 🎯 Objectives

* Clean and preprocess customer data.
* Analyze customer characteristics.
* Apply K-Means clustering.
* Determine an appropriate number of clusters using the Elbow Method.
* Group customers based on Annual Income and Spending Score.
* Visualize the identified customer segments.
* Generate a clustered customer dataset for further analysis.

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Scikit-learn**
* **Machine Learning**
* **K-Means Clustering**

---

## 📂 Project Structure

```text
Customer-Segmentation-Project/
│
├── Dataset/
│   ├── customers.csv
│   └── cleaned_customers.csv
│
├── Python/
│   ├── data_preprocessing.py
│   ├── clustering.py
│   ├── visualization.py
│   └── main.py
│
├── Output/
│   ├── elbow_method.png
│   └── clustered_customers.csv
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

The dataset contains customer information including:

| Feature       | Description                |
| ------------- | -------------------------- |
| CustomerID    | Unique customer identifier |
| Gender        | Customer gender            |
| Age           | Customer age               |
| AnnualIncome  | Annual income              |
| SpendingScore | Customer spending score    |

---

## 🔄 Project Workflow

```text
Customer Dataset
       ↓
Data Preprocessing
       ↓
Data Cleaning
       ↓
Feature Selection
       ↓
Elbow Method
       ↓
K-Means Clustering
       ↓
Customer Segmentation
       ↓
Visualization
       ↓
Final Clustered Dataset
```

---

## 🤖 Machine Learning Algorithm

### K-Means Clustering

K-Means is an unsupervised Machine Learning algorithm used to divide data points into a predefined number of clusters.

In this project, the following features are used:

* Annual Income
* Spending Score

The project uses the **Elbow Method** to analyze different values of K and selects **5 clusters** for customer segmentation.

---

## 📈 Elbow Method

The Elbow Method is used to determine a suitable number of clusters by analyzing the Within-Cluster Sum of Squares (WCSS).

The generated graph is saved as:

```text
Output/elbow_method.png
```

---

## 👥 Customer Segmentation

The K-Means algorithm assigns each customer to a cluster based on their Annual Income and Spending Score.

The final clustered dataset is saved as:

```text
Output/clustered_customers.csv
```

---

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/vindhyareddy031/Customer-Segmentation-Project.git
```

### 2. Open the project

```bash
cd Customer-Segmentation-Project
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

For Windows:

```bash
.venv\Scripts\activate
```

### 5. Install required libraries

```bash
pip install -r requirements.txt
```

### 6. Go to the Python folder

```bash
cd Python
```

### 7. Run data preprocessing

```bash
python data_preprocessing.py
```

### 8. Run K-Means clustering

```bash
python clustering.py
```

### 9. Run visualization

```bash
python visualization.py
```

---

## 📁 Output

The project generates:

* Cleaned customer dataset
* Clustered customer dataset
* Elbow Method visualization
* Customer segmentation visualization

---

## 💡 Business Applications

Customer segmentation can help businesses:

* Identify high-value customers.
* Develop targeted marketing campaigns.
* Understand customer purchasing behavior.
* Improve customer engagement.
* Design personalized offers.
* Support data-driven business decisions.

---

## 🚀 Future Improvements

* Use a larger real-world customer dataset.
* Add more customer features.
* Build an interactive Streamlit dashboard.
* Add Power BI visualizations.
* Compare K-Means with other clustering algorithms.
* Deploy the project as a web application.

---

## 👩‍💻 Author

**Vindhya Reddy**

GitHub: [@vindhyareddy031](https://github.com/vindhyareddy031)

---

## ⭐ Project Status

**Completed**
