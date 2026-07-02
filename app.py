import streamlit as st

from components.ai_forecast import show_ai_forecast
from components.charts import (
    show_revenue_chart,
    show_profit_chart,
    show_city_chart,
    show_payment_chart,
    show_monthly_trend,
    show_top_customers,
    show_top_products_profit,
    show_top_selling_products,
    show_customer_segmentation
)
from components.data_loader import load_data
from components.data_quality import show_data_quality
from components.executive_summary import show_executive_summary
from components.filters import apply_filters
from components.insights import show_business_insights
from components.kpi import display_kpis
from components.recommendations import show_recommendations


# Page Configuration

st.set_page_config(
    page_title="RetailIQ",
    page_icon="📊",
    layout="wide"
)

# Schema Validation Dialog

if "schema_error" not in st.session_state:
    st.session_state.schema_error = False


@st.dialog("⚠️ Invalid Dataset")
def schema_error_dialog():

    st.error("Dataset schema doesn't match the required RetailIQ dataset.")

    st.info("Showing the default RetailIQ dataset.")

    if st.button("OK"):
        st.session_state.schema_error = False
        st.rerun()


# Sidebar

st.sidebar.header("📂 Dataset Upload")

with st.sidebar.expander("📋 Required Dataset Schema"):

    st.markdown("""
    Required Columns:

    - Order_Date
    - Customer_Name
    - Product
    - Category
    - City
    - Quantity
    - Revenue
    - Profit
    - Payment_Method
    """)

uploaded_file = st.sidebar.file_uploader(
    "Upload Retail Dataset"
)

# Load Dataset

df = load_data()

if uploaded_file is not None:

    try:
        df = load_data(uploaded_file)

    except ValueError:
        st.session_state.schema_error = True

if st.session_state.schema_error:
    schema_error_dialog()

df = apply_filters(df)

# Dashboard Header

st.title("📊 RetailIQ - Business Intelligence Platform")
st.caption("Professional Retail Analytics Dashboard")

st.divider()

# Dashboard Tabs

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "📋 Data",
    "📊 Executive",
    "📈 Sales",
    "👥 Customers",
    "📦 Products",
    "📊 Analytics",
    "🤖 AI Forecast"
])

#  Data 

with tab1:

    st.success("✅ RetailIQ Dataset Loaded")

    st.subheader("📋 Sales Dataset")

    st.dataframe(df, width="stretch")

    show_data_quality(df)

    st.divider()

    st.subheader("📤 Export Data")

    csv = df.to_csv(index=False)

    st.download_button(
        label="⬇ Download Filtered CSV",
        data=csv,
        file_name="RetailIQ_Filtered_Data.csv",
        mime="text/csv"
    )

#  Executive 

with tab2:

    display_kpis(df)

    st.divider()

    show_executive_summary(df)

    st.divider()

    show_business_insights(df)

    st.divider()

    show_recommendations(df)

    st.divider()

    show_customer_segmentation(df)

#  Sales 

with tab3:

    st.subheader("📈 Sales Analytics")

    col1, col2 = st.columns(2)

    with col1:
        show_revenue_chart(df)

    with col2:
        show_profit_chart(df)

    st.divider()

    st.subheader("📈 Monthly Revenue vs Profit Trend")

    show_monthly_trend(df)

#  Customers 

with tab4:

    st.subheader("👥 Customer Analytics")

    show_top_customers(df)

#  Products

with tab5:

    st.subheader("📦 Product Analytics")

    show_top_products_profit(df)

    st.divider()

    show_top_selling_products(df)

#  Business Analytics 

with tab6:

    st.subheader("📊 Business Analytics")

    col1, col2 = st.columns(2)

    with col1:
        show_city_chart(df)

    with col2:
        show_payment_chart(df)

#  AI Forecast 

with tab7:

    show_ai_forecast(df)