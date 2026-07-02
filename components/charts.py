import streamlit as st
import plotly.express as px


# Dashboard Charts

def show_revenue_chart(df):

    category_sales = (
        df.groupby("Category")["Revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    fig = px.bar(
        x=category_sales.index,
        y=category_sales.values,
        labels={"x": "Category", "y": "Revenue"},
        title="Revenue by Category"
    )

    st.plotly_chart(fig, use_container_width=True)


def show_profit_chart(df):

    category_profit = (
        df.groupby("Category")["Profit"]
        .sum()
        .sort_values(ascending=False)
    )

    fig = px.bar(
        x=category_profit.index,
        y=category_profit.values,
        labels={"x": "Category", "y": "Profit"},
        title="Profit by Category"
    )

    st.plotly_chart(fig, use_container_width=True)


def show_city_chart(df):

    city_revenue = (
        df.groupby("City")["Revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    st.write("### Revenue by City")

    st.bar_chart(city_revenue)


def show_payment_chart(df):

    payment_sales = (
        df.groupby("Payment_Method")["Revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    st.write("### Revenue by Payment Method")

    st.bar_chart(payment_sales)


def show_monthly_trend(df):

    monthly_data = (
        df.groupby(df["Order_Date"].dt.to_period("M"))
        [["Revenue", "Profit"]]
        .sum()
        .reset_index()
    )

    monthly_data["Order_Date"] = monthly_data["Order_Date"].astype(str)

    fig = px.line(
        monthly_data,
        x="Order_Date",
        y=["Revenue", "Profit"],
        title="Monthly Revenue vs Profit Trend",
        markers=True
    )

    st.plotly_chart(fig, use_container_width=True)


def show_top_customers(df):

    top_customers = (
        df.groupby("Customer_Name")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        top_customers,
        x="Revenue",
        y="Customer_Name",
        orientation="h",
        title="Top 10 Customers by Revenue"
    )

    fig.update_layout(
        yaxis=dict(autorange="reversed")
    )

    st.plotly_chart(fig, use_container_width=True)


def show_top_products_profit(df):

    top_products = (
        df.groupby("Product")["Profit"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        top_products,
        x="Profit",
        y="Product",
        orientation="h",
        title="Top 10 Products by Profit"
    )

    fig.update_layout(
        yaxis=dict(autorange="reversed")
    )

    st.plotly_chart(fig, use_container_width=True)


def show_top_selling_products(df):

    top_products = (
        df.groupby("Product")["Quantity"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        top_products,
        x="Quantity",
        y="Product",
        orientation="h",
        title="Top 10 Selling Products"
    )

    fig.update_layout(
        yaxis=dict(autorange="reversed")
    )

    st.plotly_chart(fig, use_container_width=True)


# Customer Segmentation

def show_customer_segmentation(df):

    customer_sales = (
        df.groupby("Customer_Name")["Revenue"]
        .sum()
        .reset_index()
    )

    customer_sales = customer_sales.sort_values(
        "Revenue",
        ascending=False
    ).reset_index(drop=True)

    total = len(customer_sales)

    vip_limit = int(total * 0.30)
    regular_limit = int(total * 0.70)

    segments = []

    for i in range(total):

        if i < vip_limit:
            segments.append("VIP")

        elif i < regular_limit:
            segments.append("Regular")

        else:
            segments.append("Low Value")

    customer_sales["Segment"] = segments

    customer_sales.insert(
        0,
        "Rank",
        range(1, len(customer_sales) + 1)
    )

    segment_summary = (
        customer_sales["Segment"]
        .value_counts()
        .reset_index()
    )

    segment_summary.columns = ["Segment", "Customers"]

    st.subheader("👥 Customer Segmentation")

    col1, col2, col3 = st.columns(3)

    vip = customer_sales[
        customer_sales["Segment"] == "VIP"
    ].shape[0]

    regular = customer_sales[
        customer_sales["Segment"] == "Regular"
    ].shape[0]

    low = customer_sales[
        customer_sales["Segment"] == "Low Value"
    ].shape[0]

    with col1:
        st.metric("🥇 VIP Customers", vip)

    with col2:
        st.metric("🥈 Regular Customers", regular)

    with col3:
        st.metric("🥉 Low Value Customers", low)

    fig = px.bar(
        segment_summary,
        x="Segment",
        y="Customers",
        color="Segment",
        text="Customers",
        title="Customer Distribution by Segment"
    )

    fig.update_layout(showlegend=False)

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📋 Customer Segmentation Table")

    st.dataframe(
        customer_sales[
            ["Rank", "Customer_Name", "Revenue", "Segment"]
        ],
        use_container_width=True
    )