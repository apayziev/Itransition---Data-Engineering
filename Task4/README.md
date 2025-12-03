# Book Orders Data Analysis - Task 4

This project analyzes book order data from three different datasets (DATA1, DATA2, DATA3) and produces a professional BI dashboard.

## 📊 Dashboard

The dashboard is available in the `dashboard/` folder. You can view it by:

1. **Local viewing**: Open `dashboard/index.html` in a web browser
2. **GitHub Pages**: Deploy the `dashboard/` folder to GitHub Pages
3. **Any static hosting**: Upload the `dashboard/` folder to any static file hosting service

### Dashboard Features:
- Three tabs for DATA1, DATA2, and DATA3
- Key metrics cards (Unique Users, Author Sets, Popular Author, Top Customer)
- Top 5 Days by Revenue table
- Best Buyer with all associated user IDs
- Interactive Daily Revenue Chart

## 📁 Project Structure

```
Task4/
├── analysis.ipynb          # Jupyter notebook with complete analysis
├── dashboard/
│   ├── index.html         # Interactive dashboard
│   └── dashboard_data.json # Data for the dashboard
├── data/
│   ├── DATA1/
│   │   ├── users.csv
│   │   ├── books.yaml
│   │   └── orders.parquet
│   ├── DATA2/
│   │   └── ...
│   └── DATA3/
│       └── ...
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🔧 Installation

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

## 🚀 Running the Analysis

1. Open `analysis.ipynb` in Jupyter Notebook or VS Code
2. Run all cells to perform the analysis
3. Results will be saved to `dashboard_data.json`

## 📈 Analysis Results Summary

### DATA1
| Metric | Value |
|--------|-------|
| Top 5 Days by Revenue | 2025-01-02, 2024-11-14, 2024-09-06, 2024-11-09, 2024-10-07 |
| Unique Users | 3,115 |
| Unique Author Sets | 325 |
| Most Popular Author | Arlinda Huel |
| Top Customer IDs | [44850, 45062, 46955] |
| Top Customer Spending | $1,386.76 |

### DATA2
| Metric | Value |
|--------|-------|
| Top 5 Days by Revenue | 2024-09-12, 2024-11-15, 2024-11-21, 2024-12-25, 2025-01-20 |
| Unique Users | 2,663 |
| Unique Author Sets | 293 |
| Most Popular Author | Jaimie Skiles |
| Top Customer IDs | [53583, 55058, 55420] |
| Top Customer Spending | $1,312.84 |

### DATA3
| Metric | Value |
|--------|-------|
| Top 5 Days by Revenue | 2024-11-16, 2025-01-31, 2024-10-26, 2024-11-12, 2024-11-01 |
| Unique Users | 3,290 |
| Unique Author Sets | 268 |
| Most Popular Author | Benjamin Mills |
| Top Customer IDs | [49715, 50963] |
| Top Customer Spending | $1,207.48 |

## 📝 Analysis Details

### Data Cleaning
- Parsed various date/time formats using `python-dateutil`
- Handled multiple currency formats (USD, EUR with different notations like `$`, `€`, `¢`)
- Converted EUR to USD using rate €1 = $1.2
- Handled NULL values and missing data

### User Reconciliation
Users were reconciled using a Union-Find algorithm that groups users who:
- Share the same email (primary identifier)
- Share the same phone number
- Match on at least 3 out of 4 fields (name, address, phone, email)

This accounts for users who may have changed their address, phone, or used an alias.

### Author Set Analysis
Author sets were determined by splitting the author field by commas and creating unique tuples of sorted author names. Each unique combination counts as one author set.

### Top Customer Identification
Total spending was aggregated across all user IDs belonging to the same reconciled user group to identify the top customer.

## 🛠️ Technologies Used

- **Python 3.12**: Core programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical operations
- **Matplotlib**: Chart generation
- **PyYAML**: YAML file parsing
- **PyArrow**: Parquet file reading
- **Bootstrap 5**: Dashboard UI framework
- **Chart.js**: Interactive charts

## 📧 Contact

For questions or feedback, please reach out to the project maintainer.
