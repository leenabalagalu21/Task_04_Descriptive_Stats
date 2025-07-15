import polars as pl

# Path to your CSV
file_path = r"C:\Users\leena\OneDrive\Desktop\RA\assignmt 4\netflix_titles.csv"
df = pl.read_csv(file_path)

# ── 1) Extract numeric duration from the "duration" column ─────────────
df = df.with_columns([
    pl.col("duration")
      .str.extract(r"(\d+)", 1)
      .cast(pl.Int64)
      .alias("duration_minutes")
])

# ── 2) Numeric Analysis ────────────────────────────────────────────────
print("\n--- Numeric Analysis ---")
print(df.select(["release_year", "duration_minutes"]).describe())

# ── 3) Categorical Analysis via group_by/count ─────────────────────────
print("\n--- Categorical Analysis ---")
cat_fields = ["type", "rating", "country", "listed_in"]

for col in cat_fields:
    # how many distinct values?
    unique_count = df.select(pl.col(col)).n_unique()

    # count frequency of each category
    freq = (
        df.filter(pl.col(col).is_not_null())
          .group_by(col)
          .agg(pl.count().alias("count"))
          .sort("count", descending=True)
    )

    if freq.height > 0:
        top_value, top_count = freq.row(0)
        print(f"\n{col} - Unique: {unique_count}")
        print(f"Most Frequent: {top_value} ({top_count} times)")
    else:
        print(f"\n{col} - No valid data")
