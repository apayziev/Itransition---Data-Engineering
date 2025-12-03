# Task 4 - Book Orders Analysis

Data analysis project for book orders from three datasets.

## What it does

- Loads data from CSV, YAML, and Parquet files
- Cleans messy data (different date formats, currency symbols, etc.)
- Finds unique users by matching emails and phone numbers
- Calculates daily revenue and finds top 5 days
- Identifies best-selling authors and top customers
- Creates a dashboard to visualize results

## How to run

```bash
# Setup
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run analysis
# Open analysis.ipynb and run all cells
```

## Files

- `analysis.ipynb` - main analysis notebook
- `docs/` - HTML dashboard (deployed via GitHub Pages)
- `data/` - input data (DATA1, DATA2, DATA3)

## Results

| Dataset | Unique Users | Author Sets | Top Customer Spending |
|---------|-------------|-------------|----------------------|
| DATA1 | 3,115 | 325 | $1,386.76 |
| DATA2 | 2,663 | 293 | $1,312.84 |
| DATA3 | 3,290 | 268 | $1,207.48 |

## Notes

- EUR converted to USD at rate 1.2
- Users with same email or phone are counted as one person
- Co-authored books credit each author separately
