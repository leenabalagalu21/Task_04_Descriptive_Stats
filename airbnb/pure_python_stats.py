import csv
import math
from collections import Counter, defaultdict
from statistics import mean, stdev

def read_csv(filepath):
    with open(filepath, newline='', encoding='utf-8') as file:
        return list(csv.DictReader(file))

def is_float(value):
    try:
        float(value)
        return True
    except:
        return False

def analyze_numeric(data, fields):
    for field in fields:
        values = [float(row[field]) for row in data if is_float(row[field])]
        if not values:
            print(f"{field}: No numeric data")
            continue
        print(f"{field}: Count={len(values)}, Mean={mean(values):.2f}, Min={min(values)}, Max={max(values)}, StdDev={stdev(values) if len(values)>1 else 0}")

def analyze_categorical(data, fields):
    for field in fields:
        values = [row[field] for row in data if row[field]]
        counter = Counter(values)
        most_common = counter.most_common(1)[0] if counter else ("None", 0)
        print(f"{field}: Unique={len(counter)}, Most Frequent={most_common[0]} ({most_common[1]} times)")

def group_by_and_analyze(data, group_keys, numeric_fields):
    grouped = defaultdict(list)
    for row in data:
        key = tuple(row[k] for k in group_keys)
        grouped[key].append(row)
    
    for group, rows in grouped.items():
        label = ', '.join([f"{k}={v}" for k, v in zip(group_keys, group)])
        print(f"\n--- Group: {label} ---")
        analyze_numeric(rows, numeric_fields)

if __name__ == "__main__":
    file_path = r"C:\Users\leena\OneDrive\Desktop\RA\assignmt 4\airbnb\AB_NYC_2019.csv"
    data = read_csv(file_path)

    numeric_fields = [
        'price', 'minimum_nights', 'number_of_reviews', 'reviews_per_month',
        'latitude', 'longitude', 'availability_365', 'calculated_host_listings_count'
    ]
    cat_fields = ['neighbourhood_group', 'neighbourhood', 'room_type']

    print("\n--- Overall Numeric Analysis ---")
    analyze_numeric(data, numeric_fields)

    print("\n--- Overall Categorical Analysis ---")
    analyze_categorical(data, cat_fields)

    print("\n=== Grouped by 'neighbourhood_group' ===")
    group_by_and_analyze(data, ['neighbourhood_group'], numeric_fields)

    print("\n=== Grouped by 'room_type' ===")
    group_by_and_analyze(data, ['room_type'], numeric_fields)

    print("\n=== Grouped by 'neighbourhood_group' and 'room_type' ===")
    group_by_and_analyze(data, ['neighbourhood_group', 'room_type'], numeric_fields)