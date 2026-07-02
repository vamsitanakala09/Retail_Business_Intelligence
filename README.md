# 📊 RetailIQ – Business Intelligence Platform

RetailIQ is an interactive Business Intelligence dashboard built using **Python**, **Streamlit**, **MySQL**, and **Machine Learning**. It enables users to analyze retail sales data, monitor key business metrics, visualize trends, and generate AI-powered sales forecasts through an intuitive web interface.

This project was developed as a portfolio project to demonstrate practical Data Analytics, Data Visualization, Database Management, and Business Intelligence skills.

---

# 🚀 Features

- 📈 Executive Business Dashboard
- 💰 Sales Performance Analysis
- 👥 Customer Analysis
- 📦 Product Analysis
- 📊 Business Analytics Dashboard
- 🤖 AI-Powered Sales Forecast
- 📊 Data Quality Report
- 💡 Business Recommendations
- 📤 Export Reports (CSV)
- 🔍 Interactive Dashboard Filters
- 🗄️ MySQL Database Integration
- ⚡ Interactive Plotly Visualizations
- 📱 Responsive Streamlit Interface

---
# 📸 Dashboard Preview

## 📊 Executive Dashboard

![Executive Dashboard](screenshots/executive_dashboard.png)

---

## 📈 Sales Dashboard

![Sales Dashboard](screenshots/sales_dashboard.png)

---

## 👥 Customer Dashboard

![Customer Dashboard](screenshots/customer_dashboard.png)

---

## 📦 Product Dashboard

![Product Dashboard](screenshots/product_dashboard.png)

---

## 📊 Business Analytics

![Business Analytics](screenshots/analytics_dashboard.png)

---

## 🤖 AI Sales Forecast

---

![AI Sales Forecast](screenshots/ai_forecast.png)

# 🛠️ Tech Stack

### Programming Language
- Python

### Framework
- Streamlit

### Database
- MySQL

### Libraries
- Pandas
- Plotly
- Scikit-learn
- NumPy
- Python-dotenv
- MySQL Connector

---

# 📂 Project Structure

```
Retail_Business_Intelligence/
│
├── components/
│   ├── ai_forecast.py
│   ├── charts.py
│   ├── data_loader.py
│   ├── data_quality.py
│   ├── executive_summary.py
│   ├── export.py
│   ├── filters.py
│   ├── insights.py
│   ├── kpi.py
│   └── recommendations.py
│
├── data/
│   └── raw/
│
├── screenshots/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── generate_dataset.py
└── import_to_mysql.py
```

---

# 📊 Dashboard Modules

### 📈 Executive Dashboard

Monitor overall business performance through KPIs and executive-level insights.

### 💰 Sales Analysis

Analyze revenue trends, profit, monthly performance, and category-wise sales.

### 👥 Customer Analysis

Explore customer purchasing behavior and buying patterns.

### 📦 Product Analysis

Identify top-performing products and product categories.

### 🤖 AI Sales Forecast

Predict future sales using Machine Learning (Linear Regression).

### 📊 Data Quality

Validate dataset quality and identify missing or inconsistent values.

### 💡 Recommendations

Generate business insights and recommendations based on sales performance.

### 📤 Export

Export processed reports for further analysis.

---

# ⚙️ Installation

## Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_LINK>
```

## Navigate to the project

```bash
cd Retail_Business_Intelligence
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

Create a `.env` file in the project root and add your MySQL credentials.

Example:

```env
DB_HOST=localhost
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=RetailIQ
DB_PORT=3306
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

---

# 🗄️ Database

This project uses a MySQL database for storing and retrieving retail sales data.

The dataset is imported into MySQL using:

```
import_to_mysql.py
```

---

# 📸 Dashboard Preview

Dashboard screenshots will be added here.

Example:

```
screenshots/
├── executive_dashboard.png
├── sales_dashboard.png
├── customer_dashboard.png
├── product_dashboard.png
└── ai_forecast.png
```

---

# 🔮 Future Improvements

- Advanced Machine Learning Forecasting
- Customer Segmentation
- Inventory Analytics
- Profit Forecasting
- User Authentication
- Cloud Deployment
- Automated Report Scheduling

---

# 📚 Skills Demonstrated

- Python Programming
- Data Analysis
- Business Intelligence
- Data Visualization
- Machine Learning
- SQL & MySQL
- Streamlit Development
- Dashboard Design
- Data Cleaning
- Analytical Thinking

---

# 👨‍💻 Author

**Vamsi Tanakala**

Aspiring Data Analyst passionate about building interactive dashboards and solving business problems using data.

---

# ⭐ If you like this project

Please consider giving it a ⭐ on GitHub.