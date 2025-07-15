import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
file_path = r"C:\Users\leena\OneDrive\Desktop\RA\assignmt 4\airbnb\AB_NYC_2019.csv"
df = pd.read_csv(file_path)

# Convert fields
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df['reviews_per_month'] = pd.to_numeric(df['reviews_per_month'], errors='coerce')
df['availability_365'] = pd.to_numeric(df['availability_365'], errors='coerce')

# Filter out extreme outliers
df_filtered = df[df['price'] < 500]

sns.set(style="whitegrid")

# 1. Room Type Distribution
plt.figure(figsize=(7, 4))
sns.countplot(data=df, x='room_type', order=df['room_type'].value_counts().index, palette='Set2')
plt.title('Room Type Distribution')
plt.tight_layout()
plt.savefig('1_room_type_distribution.png')
plt.close()

# 2. Price by Neighbourhood Group
plt.figure(figsize=(8, 5))
sns.boxplot(data=df_filtered, x='neighbourhood_group', y='price', palette='Pastel1')
plt.title('Price Distribution by Neighbourhood Group (< $500)')
plt.tight_layout()
plt.savefig('2_price_by_neighbourhood_group.png')
plt.close()

# 3. Reviews per Month
plt.figure(figsize=(7, 4))
sns.histplot(df['reviews_per_month'].dropna(), kde=True, bins=30, color='lightblue')
plt.title('Distribution of Reviews per Month')
plt.tight_layout()
plt.savefig('3_reviews_per_month.png')
plt.close()

# 4. Availability by Room Type
plt.figure(figsize=(8, 5))
sns.boxplot(data=df[df['availability_365'] > 0], x='room_type', y='availability_365', palette='Set3')
plt.title('Availability by Room Type')
plt.tight_layout()
plt.savefig('4_availability_by_room_type.png')
plt.close()

# 5. Top 10 Neighborhoods by Listing Count
top_neigh = df['neighbourhood'].value_counts().nlargest(10)
plt.figure(figsize=(8, 5))
sns.barplot(x=top_neigh.values, y=top_neigh.index, palette='coolwarm')
plt.title('Top 10 Neighborhoods by Listing Count')
plt.xlabel('Listings')
plt.tight_layout()
plt.savefig('5_top_neighbourhoods.png')
plt.close()

# 6. Price Histogram
plt.figure(figsize=(7, 4))
sns.histplot(df_filtered['price'], bins=40, kde=True, color='orange')
plt.title('Price Distribution (< $500)')
plt.tight_layout()
plt.savefig('6_price_distribution.png')
plt.close()

print(" 6 Key visualizations saved as PNGs ")