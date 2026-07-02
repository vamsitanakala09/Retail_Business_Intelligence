import pandas as pd
import streamlit as st


def apply_filters(df):

    # Sidebar

    st.sidebar.title("📊 RetailIQ")
    st.sidebar.divider()

    st.sidebar.subheader("🔍 Dashboard Filters")

    # City Filter

    selected_city = st.sidebar.selectbox(
        "Select City",
        ["All"] + sorted(df["City"].unique()),
        key="city_filter"
    )

    if selected_city != "All":
        df = df[df["City"] == selected_city]

    # Category Filter

    selected_category = st.sidebar.selectbox(
        "Select Category",
        ["All"] + sorted(df["Category"].unique()),
        key="category_filter"
    )

    if selected_category != "All":
        df = df[df["Category"] == selected_category]

    # Payment Method Filter

    selected_payment = st.sidebar.selectbox(
        "Select Payment Method",
        ["All"] + sorted(df["Payment_Method"].unique()),
        key="payment_filter"
    )

    if selected_payment != "All":
        df = df[df["Payment_Method"] == selected_payment]

    # Product Filter

    selected_product = st.sidebar.selectbox(
        "Select Product",
        ["All"] + sorted(df["Product"].unique()),
        key="product_filter"
    )

    if selected_product != "All":
        df = df[df["Product"] == selected_product]

    # Date Filter

    st.sidebar.subheader("📅 Date Filter")

    min_date = df["Order_Date"].min()
    max_date = df["Order_Date"].max()

    selected_dates = st.sidebar.date_input(
        "Select Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
        key="date_filter"
    )

    if len(selected_dates) == 2:

        start_date, end_date = selected_dates

        df = df[
            (df["Order_Date"] >= pd.Timestamp(start_date))
            &
            (df["Order_Date"] <= pd.Timestamp(end_date))
        ]

    return df