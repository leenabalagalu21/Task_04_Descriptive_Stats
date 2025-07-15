import polars as pl

# Load dataset
file_path = r"C:\Users\leena\OneDrive\Desktop\RA\assignmt 4\airbnb\AB_NYC_2019.csv"
df = pl.read_csv(file_path)

# Fields
numeric_fields = [
    'price', 'minimum_nights', 'number_of_reviews', 'reviews_per_month',
    'latitude', 'longitude', 'availability_365', 'calculated_host_listings_count'
]
cat_fields = ['neighbourhood_group', 'neighbourhood', 'room_type']

# --- Numeric Analysis ---
print("\n -- Numeric Analysis --")
print(df.select(numeric_fields).describe())

# --- Categorical Analysis ---
print("\n -- Categorical Analysis --")
for col in cat_fields:
    unique_count = df.select(pl.col(col)).n_unique()
    vc_df = df.select(pl.col(col)).to_series().value_counts()
    
    # Sort safely
    col_name = vc_df.columns[0]
    count_col = vc_df.columns[1]
    vc_df_sorted = vc_df.sort(count_col, descending=True)

    print(f"\n{col} - Unique: {unique_count}")
    if vc_df_sorted.height > 0:
        most_common = vc_df_sorted.row(0)
        print(f"Most Frequent: {most_common[0]} ({most_common[1]} times)")
    else:
        print("Most Frequent: No values found")
