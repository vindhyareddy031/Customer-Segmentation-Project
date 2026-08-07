import streamlit as st
import pandas as pd
import plotly.express as px


# Page Configuration

st.set_page_config(
    page_title="Customer Segmentation Dashboard",
    page_icon="🛍️",
    layout="wide"
)


# Title

st.title("🛍️ Customer Segmentation Dashboard")
st.write("Analyze customer behavior using K-Means clustering")


# Load Data

df = pd.read_csv("Output/final_customer_segments.csv")


# Sidebar Filters

st.sidebar.header("Filters")


gender = st.sidebar.multiselect(
    "Select Gender",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)


segment = st.sidebar.multiselect(
    "Select Customer Segment",
    options=df["Segment"].unique(),
    default=df["Segment"].unique()
)


# Apply filters

filtered_df = df[
    (df["Gender"].isin(gender)) &
    (df["Segment"].isin(segment))
]



# KPI Cards

col1, col2, col3, col4 = st.columns(4)


col1.metric(
    "Total Customers",
    len(filtered_df)
)


col2.metric(
    "Average Income",
    round(filtered_df["AnnualIncome"].mean(),2)
)


col3.metric(
    "Average Spending Score",
    round(filtered_df["SpendingScore"].mean(),2)
)


col4.metric(
    "Number of Segments",
    filtered_df["Segment"].nunique()
)



# Gender Distribution

st.subheader("👥 Customer Distribution by Gender")


gender_count = filtered_df["Gender"].value_counts().reset_index()

gender_count.columns = [
    "Gender",
    "Count"
]


gender_chart = px.bar(
    gender_count,
    x="Gender",
    y="Count",
    title="Gender Distribution"
)


st.plotly_chart(gender_chart, width="stretch")


# Customer Segment Visualization

st.subheader("🎯 Customer Segmentation")


segment_chart = px.scatter(
    filtered_df,
    x="AnnualIncome",
    y="SpendingScore",
    color="Segment",
    size="Age",
    hover_data=[
        "CustomerID",
        "Gender",
        "Age",
        "Segment"
    ],
    title="Income vs Spending Score"
)


st.plotly_chart(
    segment_chart,
    use_container_width=True
)



# Customer Count by Segment

st.subheader("📊 Customers in Each Segment")


segment_count = (
    filtered_df["Segment"]
    .value_counts()
    .reset_index()
)


segment_count.columns = [
    "Segment",
    "Count"
]


segment_bar = px.bar(
    segment_count,
    x="Segment",
    y="Count",
    title="Customer Segment Distribution"
)


st.plotly_chart(
    segment_bar,
    use_container_width=True
)



# Average Income by Segment

st.subheader("💰 Average Income by Segment")


income_segment = (
    filtered_df
    .groupby("Segment")["AnnualIncome"]
    .mean()
    .reset_index()
)


income_chart = px.bar(
    income_segment,
    x="Segment",
    y="AnnualIncome",
    title="Average Income per Segment"
)


st.plotly_chart(
    income_chart,
    use_container_width=True
)



# Average Spending Score by Segment

st.subheader("⭐ Average Spending Score by Segment")


spending_segment = (
    filtered_df
    .groupby("Segment")["SpendingScore"]
    .mean()
    .reset_index()
)


spending_chart = px.bar(
    spending_segment,
    x="Segment",
    y="SpendingScore",
    title="Average Spending Score per Segment"
)


st.plotly_chart(
    spending_chart,
   width="stretch"
)



# Customer Data Table

st.subheader("📋 Customer Details")


st.dataframe(
    filtered_df,
    width="stretch"
)



# Download Button

csv = filtered_df.to_csv(index=False)


st.download_button(
    label="📥 Download Customer Report",
    data=csv,
    file_name="customer_segment_report.csv",
    mime="text/csv"
)