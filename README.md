# Task_04_Descriptive_Stats

## Overview

This repository contains descriptive statistical analysis scripts for two datasets:
1. **Airbnb NYC 2019 Dataset** 
2. **Netflix Titles Dataset**

The analyses are implemented using:
- Pure Python
- Pandas
- Polars

Each dataset has its own dedicated set of scripts for numerical and categorical analysis, as well as optional group-based summarizations.

---

## Repository Structure

```
.
├── airbnb/
│   ├── pure_python_stats.py
│   ├── pandas_stats.py
│   ├── polars_stats.py
│   └── visualizations.py
│
├── netflix/
│   ├── pure_python_stats.py
│   ├── pandas_stats.py
│   ├── polars_stats.py
│   └── visualizations.py
│
├── README.md
└── .gitignore
```

## Dataset Information

### Airbnb Dataset:
- **Source:** https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data

### Netflix Titles Dataset:
- **Source:** https://www.kaggle.com/datasets/shivamb/netflix-shows

Place the downloaded CSV files in the respective `airbnb/` and `netflix/` folders and update the `file_path` variables in the scripts if needed.

---
## How to Run the Code

1. **Install required packages** (if not already installed):

---
pip install pandas polars matplotlib seaborn
Run Analysis Scripts:

Navigate to the respective folder and run any script:

bash
Copy
Edit
cd airbnb
python pandas_stats.py
python pure_python_stats.py
python polars_stats.py
python visualizations.py

cd ../netflix
python pandas_stats.py
python pure_python_stats.py
python polars_stats.py
python visualizations.py
Outputs:

Console statistics for numeric and categorical columns

Visualizations saved in the plots/ folder of each dataset

---

## Summary of Findings

### Airbnb NYC
- Manhattan had the most listings, but the Bronx had the cheapest prices.
- Entire homes are more expensive and most common in Manhattan.
- Hosts with many listings are more common in Manhattan.

### Netflix Titles
- Movies dominate over TV Shows.
- The U.S. produces the majority of Netflix content.
- TV Shows tend to be shorter while Movie durations are spread across a wide range.
- Ratings like TV-MA and TV-14 dominate across both types.

## Visualizations

Four visualizations were created for each dataset:

### Airbnb:
- Histogram of Price Distribution
- Boxplot of Price by Room Type
- Bar Chart of Listings per Neighbourhood Group
- Scatter Plot of Latitude vs Longitude (Geographic Density)

### Netflix:
- Bar Chart of Content Types (TV Show vs Movie)
- Histogram of Release Years
- Bar Chart of Most Common Ratings
- Boxplot of Duration in Minutes by Type
