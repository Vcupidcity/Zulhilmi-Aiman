import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Title
st.title("Finance Data Viewer")

# Load the CSV from GitHub
DATA_URL = "https://raw.githubusercontent.com/Vcupidcity/Zulhilmi-Aiman/refs/heads/main/Finance_data.csv"

@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df

data = load_data(DATA_URL)

# Show raw data
st.subheader("Raw Finance Data")
st.dataframe(data)

# Summary statistics for numeric columns
st.subheader("Summary Statistics")
st.write(data.describe(include='all'))

# Simple filtering by Gender
st.subheader("Filter by Gender")
filter_gender = st.selectbox("Select Gender to filter", options=['All'] + data['gender'].dropna().unique().tolist())
if filter_gender != 'All':
    filtered = data[data['gender'] == filter_gender]
else:
    filtered = data
st.dataframe(filtered)



# Load data
DATA_URL = "https://raw.githubusercontent.com/Vcupidcity/Zulhilmi-Aiman/refs/heads/main/Finance_data.csv"
df = pd.read_csv(DATA_URL)

st.title("Finance Data Analysis")

# Plot histogram with seaborn
st.subheader("Distribution of Age")

fig, ax = plt.subplots(figsize=(8, 6))
sns.histplot(data=df, x='age', kde=True, ax=ax)
ax.set_title('Distribution of Age')
ax.set_xlabel('Age')
ax.set_ylabel('Frequency')

st.pyplot(fig)
