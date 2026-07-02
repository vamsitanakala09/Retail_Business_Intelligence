import pandas as pd
import streamlit as st

from sqlalchemy import create_engine
from urllib.parse import quote_plus

from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv("MYSQL_HOST")
port = os.getenv("MYSQL_PORT")
user = os.getenv("MYSQL_USER")
password = quote_plus(os.getenv("MYSQL_PASSWORD"))
database = os.getenv("MYSQL_DATABASE")

# Create MySQL database connection
engine = create_engine(
    f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
)

@st.cache_data
def load_data(uploaded_file=None):

    required_columns = [
        "Order_Date",
        "Customer_Name",
        "Product",
        "Category",
        "City",
        "Quantity",
        "Revenue",
        "Profit",
        "Payment_Method"
    ]

    if uploaded_file is None:
        df = pd.read_sql("SELECT * FROM retail_sales", engine)

    else:
        filename = uploaded_file.name.lower()

        if filename.endswith(".csv"):
            df = pd.read_csv(uploaded_file)

        elif filename.endswith(".xlsx"):
            df = pd.read_excel(uploaded_file)

        else:
            raise ValueError({
                "missing": [],
                "extra": ["Unsupported file type"]
            })

        missing = set(required_columns) - set(df.columns)

        if missing:
            raise ValueError({
                "missing": list(missing),
                "extra": []
            })

    df["Order_Date"] = pd.to_datetime(df["Order_Date"])

    return df