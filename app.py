import streamlit as st
import pandas as pd

st.set_page_config(page_title="NGS QC Dashboard", layout="wide")

st.title("🧬 NGS Quality Control Dashboard")

# Upload file
uploaded_file = st.file_uploader("Upload your QC metrics CSV", type=["csv"])

# Load default sample if no file uploaded
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("File uploaded successfully!")
else:
    st.info("Using sample data from local file.")
    df = pd.read_csv("sample_data/sample_qc.csv")

# Show raw data
st.subheader("📋 Raw QC Metrics Table")
st.dataframe(df, use_container_width=True)

# Summary statistics
st.subheader("📊 Summary Statistics")
st.write(df.describe())

import matplotlib.pyplot as plt
import seaborn as sns

st.subheader("📈 Visualizations")

# Bar plot: Total Reads per Sample
st.markdown("### 🧪 Total Reads per Sample")
fig1, ax1 = plt.subplots()
sns.barplot(data=df, x="Sample_ID", y="Total_Reads", ax=ax1)
ax1.set_ylabel("Total Reads")
ax1.set_xlabel("Sample")
st.pyplot(fig1)

# Histogram: Q30 Distribution
st.markdown("### 🧬 Q30 Quality Scores Distribution")
fig2, ax2 = plt.subplots()
sns.histplot(df["Q30(%)"], bins=10, kde=True, ax=ax2)
ax2.set_xlabel("Q30 (%)")
st.pyplot(fig2)

# Boxplot: GC Content
st.markdown("### 🧬 GC Content Distribution")
fig3, ax3 = plt.subplots()
sns.boxplot(y=df["GC_Content(%)"], ax=ax3)
ax3.set_ylabel("GC Content (%)")
st.pyplot(fig3)

