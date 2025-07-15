import pandas as pd

# File path
file_path = r"C:\Users\leena\OneDrive\Desktop\RA\assignmt 4\airbnb\AB_NYC_2019.csv"

# Load dataset
df = pd.read_csv(file_path)

# Define numeric and categorical columns
numeric_fields = [
    'price', 'minimum_nights', 'number_of_reviews', 'reviews_per_month',
    'latitude', 'longitude', 'availability_365', 'calculated_host_listings_count'
]
cat_fields = ['neighbourhood_group', 'neighbourhood', 'room_type']

# --- Numeric Analysis ---
print("\n--- Numeric Analysis ---")
print(df[numeric_fields].describe())

# --- Categorical Analysis ---
print("\n--- Categorical Analysis ---")
for col in cat_fields:
    unique_vals = df[col].nunique()
    value_counts = df[col].value_counts()

    print(f"\n{col} - Unique: {unique_vals}")
    if not value_counts.empty:
        most_common = value_counts.idxmax()
        most_common_count = value_counts.max()
        print(f"Most Frequent: {most_common} ({most_common_count} times)")
    else:
        print("Most Frequent: No values found")
