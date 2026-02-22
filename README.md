# Ecommerce Analysis Project

A comprehensive data analysis and visualization project for ecommerce sales data. This project performs data cleaning, descriptive analysis, and generates insightful charts to help understand business performance.

## Project Overview

This analysis examines 171 ecommerce transactions across 5 regions and 7 product categories throughout 2024. The project identifies key trends, top performers, and areas needing operational improvement.

## Dataset

**Source:** `data/Ecommerce_Data.xlsx`

### Key Statistics
- **Total Records:** 171 transactions
- **Date Range:** January 2, 2024 - December 26, 2024
- **Product Categories:** 7
- **Regions:** 5 (North, South, East, West, Central)
- **Average Order Value:** $2,639.41
- **Order Value Range:** $40.76 - $8,758.35

### Data Fields
- OrderID
- OrderDate
- CustomerName
- Category
- Region
- Quantity
- UnitPrice ($)
- PaymentMethod
- DeliveryStatus
- TotalAmount ($)

## Project Structure

```
Ecommerce_Analysis/
├── data/
│   ├── Ecommerce_Data.xlsx          # Original raw data
│   └── ecommerce_cleaned.csv        # Cleaned data (generated)
├── scripts/
│   └── ecommerce.py                 # Main analysis script
├── outputs_charts/                  # Generated visualizations
│   ├── total_sales_per_category.png
│   ├── payment_method_distribution.png
│   ├── hist_total_amount.png
│   ├── monthly_sales_trend.png
│   └── delivery_status_by_region.png
└── README.md                        # This file
```

## Analysis Sections

### 1. Data Understanding
- Loads and inspects the dataset
- Identifies data types, unique values, and date ranges
- Reports: 7 categories, 5 regions, data from full year 2024

### 2. Data Cleaning
- Checks for missing values (none found)
- Removes duplicate records (none found)
- Fixes invalid quantity values (sets negative/zero to 1)
- Data quality: **100% clean dataset**

### 3. Descriptive Analysis
- Calculates order value statistics
- Identifies top performing category: **Fashion**
- Reports most common payment method: **PayPal**
- Counts cancelled/returned orders: **92 orders (54% issue rate)**
- Identifies highest revenue region: **South**

### 4. Customer & Product Insights
- Top 5 customers by spending
- Category average order values
- Regional sales breakdown
- Delivery success metrics
- Average order quantity: **5.09 items per order**

### 5. Visualization
Generates 5 charts for visual analysis:
- **Bar chart:** Total sales by category
- **Pie chart:** Payment method distribution
- **Histogram:** Order value distribution
- **Line chart:** Monthly sales trends
- **Stacked bar chart:** Delivery status by region

### 6. Business Insights
Key findings:
- **Top 3 Categories:** Fashion ($88.1K), Home Decor ($64.3K), Toys ($50.8K)
- **Best Payment Method:** PayPal (avg order $2,799.44)
- **Regions Needing Attention:** Central (17% delivery success), East (13% delivery success)

## Key Findings

### Top Performers
| Metric | Value |
|--------|-------|
| Top Category | Fashion |
| Top Region | South |
| Top Customer | Customer_71 ($8,758.35) |
| Best Payment Method | PayPal |

### Challenges
- **High cancellation/return rate:** 54% of orders (92 of 171)
- **Delivery issues in Central & East regions:** <27% success rate
- **Low delivery rates overall:** Only 39 out of 171 orders marked as delivered

### Recommendations
1. **Focus marketing efforts** on Fashion category (highest sales)
2. **Promote PayPal** as payment method (highest average order values)
3. **Investigate delivery operations** in Central and East regions
4. **Address cancellation/return issues** - high rate suggests potential quality or logistics problems

## Running the Analysis

### Requirements
- Python 3.8+
- pandas
- matplotlib
- openpyxl (for Excel support)

### Installation
```bash
pip install pandas matplotlib openpyxl
```

### Execution
```bash
python scripts/ecommerce.py
```

The script will:
1. Load data from `data/Ecommerce_Data.xlsx`
2. Perform cleaning and analysis
3. Generate 5 visualization charts
4. Save cleaned data to `data/ecommerce_cleaned.csv`
5. Output all charts to `outputs_charts/` folder

## Output Files

### Cleaned Data
- **File:** `data/ecommerce_cleaned.csv`
- **Format:** CSV with 10 columns and 171 rows
- **Use:** For further analysis or import into other tools

### Charts Generated
1. `total_sales_per_category.png` - Bar chart of category performance
2. `payment_method_distribution.png` - Pie chart of payment methods
3. `hist_total_amount.png` - Histogram of order values
4. `monthly_sales_trend.png` - Line chart showing sales over time
5. `delivery_status_by_region.png` - Stacked bar chart of delivery status

## Data Quality Notes

- No missing values in original dataset
- No duplicate records found
- All data types handled appropriately
- Quantity validation applied (negative values set to 1)

## Future Improvements

- Customer segmentation analysis
- Predictive modeling for order values
- Geographic heat maps
- Time series forecasting
- Cohort analysis

## Author Notes

This analysis was conducted to understand ecommerce business performance and identify key areas for improvement. The high cancellation/return rate is a significant finding that warrants further investigation into product quality, order accuracy, and customer satisfaction.

---

**Last Updated:** February 22, 2026
