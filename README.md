# Executive Sales Performance Dashboard

## 📊 Project Overview
This project demonstrates an end-to-end **data analytics workflow**, starting from raw sales data ingestion and ETL processing to building an **executive-level interactive dashboard**. The solution focuses on clean data modeling, KPI generation, and business-focused visualization.

The project is designed to reflect **real-world data analyst responsibilities**, including data cleaning, dimensional modeling, KPI logic, and dashboard design.

---

## 🛠️ Tech Stack
- **Python (Pandas)** – Data profiling, cleaning, and ETL
- **MySQL** – Data warehouse with star schema
- **Tableau Public** – Interactive executive dashboard
- **Git & GitHub** – Version control and project sharing

---

## 🗂️ Project Architecture
Raw CSV Data
↓
Python ETL (Cleaning & Transformation)
↓
MySQL Data Warehouse (Fact & Dimension Tables)
↓
Curated Analytical Dataset (CSV Export)
↓
Tableau Public Dashboard
## 🔄 ETL Pipeline
1. Ingested raw sales data from CSV
2. Performed data profiling to identify schema, data types, and missing values
3. Cleaned and transformed data using Python (Pandas)
4. Designed a **star schema** with:
   - `fact_sales`
   - `dim_customers`
   - `dim_products`
   - `dim_location`
   - `dim_date`
5. Loaded transformed data into MySQL
6. Exported an analysis-ready dataset for visualization

---

## 🧱 Data Model
- **Fact Table**
  - Sales transactions (order, product, customer, location, date, revenue)

- **Dimension Tables**
  - Customer
  - Product
  - Location
  - Date (supports YoY, MoM analysis)

This structure supports scalable KPI calculation and dashboard performance.

---

## 📈 Dashboard KPIs & Insights
The Tableau dashboard includes:

- **Total Revenue**
- **Average Order Value (AOV)**
- **Revenue Trend by Year**
- **Revenue by Category**
- **Revenue by Region**
- **Top 10 Products by Revenue**
