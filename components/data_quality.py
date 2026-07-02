import streamlit as st


def show_data_quality(df):

    st.subheader("📋 Data Quality Report")

    total_records = len(df)

    missing_values = df.isnull().sum().sum()

    duplicate_rows = df.duplicated().sum()

    total_categories = df["Category"].nunique()

    total_cities = df["City"].nunique()

    start_date = df["Order_Date"].min().strftime("%d-%b-%Y")
    end_date = df["Order_Date"].max().strftime("%d-%b-%Y")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("📦 Total Records", total_records)

        st.metric("❌ Missing Values", missing_values)

    with col2:
        st.metric("📄 Duplicate Rows", duplicate_rows)

        st.metric("🏷 Categories", total_categories)

    with col3:
        st.metric("🌍 Cities", total_cities)

        st.metric(
            "📅 Date Range",
            f"{start_date}\n{end_date}"
        )