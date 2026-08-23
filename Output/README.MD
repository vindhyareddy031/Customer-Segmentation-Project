# Customer Segmentation Project

## 📌 Project Overview

This project performs customer segmentation using **Machine Learning and K-Means Clustering**.

The goal is to analyze customer behavior and divide customers into meaningful groups based on their purchasing patterns. These customer segments can help businesses understand their customers and design better marketing strategies.

The project includes data preprocessing, exploratory data analysis (EDA), customer segmentation, cluster analysis, and an interactive **Streamlit dashboard**.

---

## 🎯 Objectives

* Clean and preprocess customer data
* Perform exploratory data analysis
* Analyze customer purchasing behavior
* Apply K-Means clustering
* Identify meaningful customer segments
* Visualize customer segments
* Build an interactive Streamlit dashboard
* Generate segment-wise analysis and insights

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Scikit-learn**
* **Plotly**
* **Streamlit**

---

## 📂 Project Structure

```text
Customer-Segmentation-Project/
│
├── Dataset/
│   └── Customer dataset files
│
├── Output/
│   ├── cluster_summary.csv
│   ├── final_customer_segments.csv
│   ├── segmented_customers.csv
│   └── requirements.txt
│
├── Python/
│   ├── app.py
│   ├── customer_segmentation.py
│   ├── data_preprocessing.py
│   ├── eda.py
│   └── segment_analysis.py
│
├── Screenshots/
│
├── .gitignore
└── README.md
```

---

## 🔄 Project Workflow

```text
Raw Customer Data
       ↓
Data Preprocessing
       ↓
Exploratory Data Analysis
       ↓
Feature Selection
       ↓
Feature Scaling
       ↓
K-Means Clustering
       ↓
Customer Segmentation
       ↓
Segment Analysis
       ↓
Streamlit Dashboard
```

---

## 📊 Exploratory Data Analysis

The EDA phase analyzes customer characteristics and purchasing behavior using:

* Distribution analysis
* Customer demographic analysis
* Spending behavior
* Correlation analysis
* Cluster visualization
* Segment-wise comparisons

---

## 🤖 Customer Segmentation

The project uses **K-Means Clustering** to group customers with similar characteristics.

The clustering process includes:

1. Selecting relevant customer features
2. Preparing the dataset
3. Scaling numerical features
4. Determining a suitable number of clusters
5. Applying K-Means clustering
6. Assigning customers to clusters
7. Analyzing the characteristics of each segment

---

## 👥 Customer Segments

The resulting clusters represent groups of customers with similar purchasing behavior.

These segments can be used to identify:

* High-value customers
* Regular customers
* Low-value customers
* Potential customers for targeted marketing
* Customers requiring retention strategies

---

## 📈 Streamlit Dashboard

The project includes an interactive Streamlit dashboard that allows users to explore customer segmentation results through charts, KPIs, and segment-level analysis.

### Dashboard Features

* Customer overview
* Customer segment distribution
* Cluster analysis
* Interactive visualizations
* Segment-wise insights
* Customer-level analysis

---

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/vindhyareddy031/Customer-Segmentation-Project.git
```

### 2. Open the project folder

```bash
cd Customer-Segmentation-Project
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment on Windows

```powershell
.venv\Scripts\activate
```

### 5. Install required libraries

```bash
pip install -r Output/requirements.txt
```

### 6. Run the Streamlit dashboard

```bash
streamlit run Python/app.py
```

The dashboard will open in your browser.

---

## 📁 Output Files

| File                          | Description                                   |
| ----------------------------- | --------------------------------------------- |
| `cluster_summary.csv`         | Summary information for each customer cluster |
| `final_customer_segments.csv` | Final customer segmentation results           |
| `segmented_customers.csv`     | Customers with their assigned cluster         |
| `requirements.txt`            | Required Python libraries                     |

---

## 💡 Business Applications

Customer segmentation can help businesses:

* Create personalized marketing campaigns
* Identify high-value customers
* Improve customer retention
* Offer targeted promotions
* Understand purchasing behavior
* Improve customer relationship management

---

## 🚀 Future Enhancements

* Deploy the dashboard online
* Add customer lifetime value analysis
* Add RFM analysis
* Add automated segment recommendations
* Add predictive customer behavior analysis
* Connect the dashboard to a live database

---

## 👩‍💻 Author

**Vindhya Reddy**

B.Tech – Artificial Intelligence & Data Science

---

## ⭐ Project

If you find this project useful, consider giving the repository a star on GitHub.


