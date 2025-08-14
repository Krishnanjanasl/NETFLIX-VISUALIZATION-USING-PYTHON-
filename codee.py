# IMPORT LIBRARIES 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import os

os.makedirs("images", exist_ok=True)

#LOAD DATASET

df=pd.read_csv(r"C:\Users\drsan\Downloads\netflix_titles.csv")

#DATA CLEANING

df['country'].fillna('Unknown', inplace=True)
df['director'].fillna('Unknown', inplace=True)
df['cast'].fillna('Unknown', inplace=True)
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')


#Movies vs TV Shows Count

plt.figure(figsize=(6,4))
sns.countplot(data=df, x='type', palette=['red', 'grey'])
plt.title("Movies vs TV Shows on Netflix")
plt.savefig("images/movies_vs_tvshows.png", dpi=300, bbox_inches="tight")
plt.close()


#Content Added Over the Years

plt.figure(figsize=(10,5))
df['release_year'].value_counts().sort_index().plot(kind='bar', color='red')
plt.title("Number of Titles Released per Year")
plt.xlabel("Release Year")
plt.ylabel("Count")
plt.savefig("images/titles_per_year.png", dpi=300, bbox_inches="tight")
plt.close()

#Top 10 Countries by Content

top_countries = df['country'].value_counts().head(10)
plt.figure(figsize=(8,5))
sns.barplot(x=top_countries.values, y=top_countries.index, palette='Reds')
plt.title("Top 10 Countries by Netflix Content")
plt.savefig("images/top_countries.png", dpi=300, bbox_inches="tight")
plt.close()

#Distribution of Ratings

order = list(df['rating'].value_counts().index)
plt.figure(figsize=(8,5))
sns.countplot(data=df, y='rating', order=order, palette='Reds')
plt.title("Distribution of Ratings on Netflix")
plt.savefig("images/ratings_distribution.png", dpi=300, bbox_inches="tight")
plt.close()

#Movie Duration Distribution

movies_df = df[df['type'] == 'Movie'].copy()
movies_df['duration_minutes'] = movies_df['duration'].str.replace(' min', '').astype(float)

plt.figure(figsize=(10,5))
sns.histplot(movies_df['duration_minutes'], bins=30, color='red')
plt.title("Movie Duration Distribution")
plt.xlabel("Minutes")
plt.savefig("images/movie_duration_distribution.png", dpi=300, bbox_inches="tight")
plt.close()

#Top 10 Genres

genre_list = []
for g in df['listed_in']:
    genre_list.extend(g.split(', '))
top_genres = pd.Series(Counter(genre_list)).sort_values(ascending=False).head(10)

plt.figure(figsize=(8,5))
sns.barplot(x=top_genres.values, y=top_genres.index, palette='Reds')
plt.title("Top 10 Genres on Netflix")
plt.savefig("images/top_genres.png", dpi=300, bbox_inches="tight")
plt.close()

#Correlation Heatmap

plt.figure(figsize=(6,4))
sns.heatmap(df.select_dtypes(include='number').corr(),
            annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.savefig("images/heatmap.png", dpi=300, bbox_inches="tight")
plt.close()




