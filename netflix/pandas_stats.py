import pandas as pd

file_path = r"C:\Users\leena\OneDrive\Desktop\RA\assignmt 4\netflix_titles.csv"
df = pd.read_csv(file_path)

# Clean numeric duration
df['duration_minutes'] = df['duration'].str.extract(r'(\d+)').astype('float')

print("\n--- Numeric Analysis ---")
print(df[['release_year', 'duration_minutes']].describe())

print("\n--- Categorical Analysis ---")
for col in ['type', 'rating', 'country', 'listed_in']:
    print(f"{col} - Unique: {df[col].nunique()}")
    print(df[col].value_counts().head(1))