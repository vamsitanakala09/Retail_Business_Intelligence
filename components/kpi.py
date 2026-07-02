import streamlit as st

def display_kpis(df):

    total_revenue = df["Revenue"].sum()
    total_profit = df["Profit"].sum()
    total_orders = len(df)
    total_customers = df["Customer_Name"].nunique()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("💰 Revenue", f"₹{total_revenue:,.0f}")

    with col2:
        st.metric("📈 Profit", f"₹{total_profit:,.0f}")

    with col3:
        st.metric("🛒 Orders", total_orders)

    with col4:
        st.metric("👥 Customers", total_customers)