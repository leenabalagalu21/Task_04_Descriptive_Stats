# Task_04_Descriptive_Stats

## Overview

This repository contains descriptive statistical analysis scripts for two datasets:
1. **Airbnb NYC 2019 Dataset** - https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data
2. **Netflix Titles Dataset** - https://www.kaggle.com/datasets/shivamb/netflix-shows

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

---

## Instructions to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/Task_04_Descriptive_Stats.git
   cd Task_04_Descriptive_Stats
   ```

2. Navigate to the folder for the dataset you'd like to analyze:
   ```bash
   cd airbnb  # or netflix
   ```

3. Run one of the analysis scripts:
   ```bash
   python pandas_stats.py
   ```

   Output will be shown in the terminal and saved figures (for visualization scripts) will be stored in the `figures/` folder.

---

## Data Sources

**Please download the datasets manually from the following links before running the code:**

- Airbnb NYC 2019 Dataset:  
  https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data

- Netflix Titles Dataset:  
  https://www.kaggle.com/datasets/shivamb/netflix-shows

Place the downloaded CSV files in the respective `airbnb/` and `netflix/` folders and update the `file_path` variables in the scripts if needed.

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
