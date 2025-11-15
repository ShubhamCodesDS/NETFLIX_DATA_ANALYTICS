import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ----------------------------
# Load Dataset
# ----------------------------
df = pd.read_csv("mymoviedb.csv", lineterminator='\n')

# Preprocessing
df['Release_Date'] = pd.to_datetime(df['Release_Date'], errors='coerce')
df['Release_Date'] = df['Release_Date'].dt.year
df.drop(['Overview', 'Original_Language', 'Poster_Url'], axis=1, inplace=True, errors='ignore')
df.dropna(inplace=True)

# Split multiple genres into separate rows
df['Genre'] = df['Genre'].str.split(', ')
df = df.explode('Genre').reset_index(drop=True)
df['Genre'] = df['Genre'].astype('category')

# ----------------------------
# Categorize Vote Average
# ----------------------------
def categorize_col(df, col, labels):
    edges = [
        df[col].describe()['min'],
        df[col].describe()['25%'],
        df[col].describe()['50%'],
        df[col].describe()['75%'],
        df[col].describe()['max']
    ]
    df[col+"_Category"] = pd.cut(df[col], edges, labels=labels, duplicates='drop')
    return df

labels = ['Not Popular', 'Below Avg', 'Average', 'Popular']
df = categorize_col(df, 'Vote_Average', labels)

# ----------------------------
# Streamlit Dashboard
# ----------------------------
st.set_page_config(page_title="Netflix Movie Analysis", layout="wide")
st.title("🎬 Netflix Movie Analysis Dashboard")

# ----------------------------
# Dataset Preview (Full)
# ----------------------------
st.subheader("📊 Full Dataset Preview")
st.dataframe(df)

# Download button
csv = df.to_csv(index=False).encode('utf-8')
st.download_button("⬇️ Download Dataset as CSV", data=csv, file_name="netflix_dataset.csv", mime="text/csv")

# ----------------------------
# Genre-wise Distribution
# ----------------------------
st.subheader("🎭 Genre-wise Movie Count")
genre_counts = df['Genre'].value_counts().reset_index()
genre_counts.columns = ['Genre', 'Movie Count']

col1, col2 = st.columns([1,2])
with col1:
    st.dataframe(genre_counts)
with col2:
    fig, ax = plt.subplots(figsize=(8,6))
    sns.barplot(y='Genre', x='Movie Count', data=genre_counts, palette="viridis", ax=ax)
    ax.set_title("Number of Movies per Genre")
    st.pyplot(fig)

# ----------------------------
# Vote Average Distribution
# ----------------------------
st.subheader("⭐ Vote Average Distribution")
fig2, ax2 = plt.subplots()
sns.countplot(y='Vote_Average', data=df, order=df['Vote_Average'].value_counts().index, color='#4287f5', ax=ax2)
ax2.set_title("Votes distribution (Exact Values)")
st.pyplot(fig2)

# ----------------------------
# Vote Average Categories
# ----------------------------
st.subheader("📊 Vote Average Categories (Not Popular / Below Avg / Average / Popular)")
category_counts = df['Vote_Average_Category'].value_counts().reset_index()
category_counts.columns = ['Category', 'Movie Count']

col3, col4 = st.columns([1,2])
with col3:
    st.dataframe(category_counts)
with col4:
    fig3, ax3 = plt.subplots()
    sns.barplot(x='Category', y='Movie Count', data=category_counts, palette="coolwarm", ax=ax3)
    ax3.set_title("Movies by Vote Average Category")
    st.pyplot(fig3)

# ----------------------------
# Release Year Distribution
# ----------------------------
st.subheader("📅 Release Year Distribution")
fig4, ax4 = plt.subplots()
df['Release_Date'].hist(ax=ax4, bins=30, color='#f54242')
ax4.set_title("Release Year Distribution")
st.pyplot(fig4)

# ----------------------------
# Top/Bottom Movies by Popularity
# ----------------------------
st.subheader("🔥 Most & Least Popular Movies")
col5, col6 = st.columns(2)

with col5:
    st.write("**Top 5 Most Popular Movies:**")
    st.dataframe(df.nlargest(5, 'Popularity'))

with col6:
    st.write("**Top 5 Least Popular Movies:**")
    st.dataframe(df.nsmallest(5, 'Popularity'))

# ----------------------------
# Top 10 Movies Overall
# ----------------------------
st.subheader("🏆 Top 10 Movies by Popularity")
top10 = df.nlargest(10, 'Popularity')[['Title', 'Popularity', 'Genre', 'Release_Date', 'Vote_Average']]
st.dataframe(top10)
