import csv
from statistics import mean, stdev
from collections import Counter, defaultdict
import re

def read_csv(filepath):
    with open(filepath, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def extract_duration(row):
    match = re.search(r"(\d+)", row.get('duration', ''))
    return int(match.group(1)) if match else None

def analyze_numeric(data, fields):
    for field in fields:
        values = [int(row[field]) for row in data if row[field].isdigit()]
        if field == 'duration':
            values = [extract_duration(row) for row in data if extract_duration(row) is not None]
        if not values:
            print(f"{field}: No valid numeric data")
            continue
        print(f"{field}: Count={len(values)}, Mean={mean(values):.2f}, Min={min(values)}, Max={max(values)}, StdDev={stdev(values):.2f}")

def analyze_categorical(data, fields):
    for field in fields:
        values = [row[field] for row in data if row[field]]
        counter = Counter(values)
        most_common = counter.most_common(1)[0] if counter else ("None", 0)
        print(f"{field}: Unique={len(counter)}, Most Frequent={most_common[0]} ({most_common[1]} times)")

if __name__ == "__main__":
    file_path = r"C:\Users\leena\OneDrive\Desktop\RA\assignmt 4\netflix_titles.csv"
    data = read_csv(file_path)

    numeric_fields = ['release_year', 'duration']
    cat_fields = ['type', 'rating', 'country', 'listed_in']

    print("\n--- Numeric Analysis ---")
    analyze_numeric(data, numeric_fields)

    print("\n--- Categorical Analysis ---")
    analyze_categorical(data, cat_fields)