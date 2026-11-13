# 🛒 Flipkart Sales Intelligence Dashboard

A fully interactive, single-file HTML business-intelligence dashboard (Power BI / Tableau style) built from the **Flipkart e-commerce sample dataset** (19,922 product listings, Dec 2015 – Jun 2016).

> Open `flipkart_sales_dashboard.html` in any modern browser. No server, no install, works offline (Chart.js and data are embedded).

## ✨ Features
- **KPI cards:** Total Sales, Total Profit (estimated), Total Orders, Average Order Value
- **Charts:** Sub-Category sales (bar), Category performance (doughnut), Brand performance (bar), Monthly sales trend (line)
- **Filters / slicers:** Month range, Sub-Category, Category, Brand
- **Worksheet drill-down:** clicking any KPI, chart bar/slice/point, chart title or filter opens a separate full-screen worksheet with summary stats, a breakdown table (click rows to drill deeper), a searchable and sortable product table and CSV export
- Every worksheet has a **✕ Close** button (or press `Esc`) to return to the dashboard
- Assumed profit-margin input and one-click **Reset filters**

## 🗂 Field mapping
The dataset is a product catalogue, so it has no city, sales rep, order or profit columns. These are mapped as follows:

| Dashboard element | Source in data |
|---|---|
| Total Sales | Sum of `discounted_price` |
| Total Orders | Count of product records |
| Average Order Value | Sales ÷ Orders |
| **Total Profit (est.)** | Sales × assumed margin (default 20%, editable in the header). The dataset has no cost data |
| City-wise chart / filter | **Sub-Category** (2nd level of `product_category_tree`) |
| Category chart / filter | **Category** (1st level of `product_category_tree`) |
| Sales Rep chart / filter | **Brand** (`brand`; missing values = "Unbranded", hidden from the Top-10 chart) |
| Month | Month of `crawl_timestamp` |

If you later have real city / rep / profit columns, replace the mapping in `build.py`.

## 🎬 Intro video
`dashboard_intro_7s.mp4` is a 7-second clip: the dashboard shows first, animates away automatically and reveals the raw data behind it.

## 🛠 Rebuild
```bash
npm i chart.js@4.4.1
python3 build.py   # reads the CSV, embeds data + Chart.js into template.html
```

## 📁 Files
`flipkart_sales_dashboard.html` · `README.md` · `dashboard_intro_7s.mp4` · `flipkart_com-ecommerce_sample.csv` (source data)
