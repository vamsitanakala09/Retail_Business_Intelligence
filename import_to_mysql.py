import os
import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("MYSQL_HOST")
port = os.getenv("MYSQL_PORT")
user = os.getenv("MYSQL_USER")
password = quote_plus(os.getenv("MYSQL_PASSWORD"))
database = os.getenv("MYSQL_DATABASE")

engine = create_engine(
    f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
)

df = pd.read_csv("data/raw/sales.csv")

df.to_sql(
    "retail_sales",
    con=engine,
    if_exists="replace",
    index=False
)

print("✅ Data imported successfully!")