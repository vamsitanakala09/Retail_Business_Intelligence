import streamlit as st

st.markdown("""
<style>

.summary-card{
    background: var(--secondary-background-color);
    padding:24px;
    border-radius:18px;
    border-left:8px solid #1f77b4;
    margin-bottom:15px;
    min-height:160px;
}

.summary-title{
    font-size:18px;
    color:var(--text-color);
    font-weight:bold;
}

.summary-value{
    font-size:24px;
    font-weight:bold;
    color:var(--text-color);
}

.summary-sub{
    font-size:16px;
    color:gray;
}

</style>
""", unsafe_allow_html=True)


def show_executive_summary(df):

    # --------------------------
    # Calculations
    # --------------------------

    category = (
        df.groupby("Category")["Revenue"]
        .sum()
    )

    city = (
        df.groupby("City")["Revenue"]
        .sum()
    )

    payment = (
        df["Payment_Method"]
        .value_counts()
    )

    customer = (
        df.groupby("Customer_Name")["Revenue"]
        .sum()
    )

    # --------------------------
    # Values
    # --------------------------

    best_category = category.idxmax()
    best_category_revenue = category.max()

    best_city = city.idxmax()
    best_city_revenue = city.max()

    top_payment = payment.idxmax()
    payment_count = payment.max()

    top_customer = customer.idxmax()
    top_customer_revenue = customer.max()

    # --------------------------
    # Title
    # --------------------------

    st.subheader("📌 Executive Summary")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(f"""
<div class="summary-card">

<div class="summary-title">
🏆 Best Category
</div>

<div class="summary-value">
{best_category}
</div>

<div class="summary-sub" style="margin-top:12px;">
Revenue
</div>

<div class="summary-value">
₹{best_category_revenue:,.0f}
</div>

</div>
""", unsafe_allow_html=True)

    with col2:

        st.markdown(f"""
<div class="summary-card">

<div class="summary-title">
🌍 Best City
</div>

<div class="summary-value">
{best_city}
</div>

<div class="summary-sub" style="margin-top:12px;">
Revenue
</div>

<div class="summary-value">
₹{best_city_revenue:,.0f}
</div>

</div>
""", unsafe_allow_html=True)
        
    col3, col4 = st.columns(2)
        
    with col3:

        st.markdown(f"""
<div class="summary-card">

<div class="summary-title">
💳 Payment Method
</div>

<div class="summary-value">
{top_payment}
</div>

<div class="summary-sub" style="margin-top:12px;">
Orders
</div>

<div class="summary-value">
{payment_count}
</div>

</div>
""", unsafe_allow_html=True)

    with col4:

        st.markdown(f"""
<div class="summary-card">

<div class="summary-title">
👤 Top Customer
</div>

<div class="summary-value">
{top_customer}
</div>

<div class="summary-sub" style="margin-top:12px;">
Revenue
</div>

<div class="summary-value">
₹{top_customer_revenue:,.0f}
</div>

</div>
""", unsafe_allow_html=True)