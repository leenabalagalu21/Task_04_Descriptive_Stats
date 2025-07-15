import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the dataset
file_path = r"C:\Users\leena\OneDrive\Desktop\RA\assignmt 4\netflix_titles.csv"
df = pd.read_csv(file_path)

# Create output directory
output_dir = r"C:\Users\leena\OneDrive\Desktop\RA\assignmt 4\figures"
os.makedirs(output_dir, exist_ok=True)

# Extract numeric duration
df['duration_minutes'] = df['duration'].str.extract(r'(\d+)').astype(float)

# Set Seaborn style
sns.set(style="whitegrid")

# ───────────────────────────────────────────────
# 1. Count of Movies vs TV Shows
plt.figure(figsize=(7, 5))
sns.countplot(x='type', data=df, palette='Set2')
plt.title("Distribution of Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "movies_vs_tvshows.png"))
plt.close()

# ───────────────────────────────────────────────
# 2. Top 10 Countries with Most Netflix Titles
plt.figure(figsize=(10, 5))
top_countries = df['country'].value_counts().dropna().head(10)
sns.barplot(x=top_countries.values, y=top_countries.index, palette='viridis')
plt.title("Top 10 Countries Producing Netflix Titles")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "top_10_countries.png"))
plt.close()

# ───────────────────────────────────────────────
# 3. Distribution of Duration for Movies
plt.figure(figsize=(8, 5))
sns.histplot(df[df['type'] == 'Movie']['duration_minutes'].dropna(), bins=30, kde=True, color="tomato")
plt.title("Distribution of Movie Durations on Netflix")
plt.xlabel("Duration (minutes)")
plt.ylabel("Number of Movies")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "movie_duration_distribution.png"))
plt.close()

# ───────────────────────────────────────────────
# 4. Count of Ratings by Type
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='rating', hue='type',
              order=df['rating'].value_counts().index, palette="pastel")
plt.title("Content Ratings by Type")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "ratings_by_type.png"))
plt.close()