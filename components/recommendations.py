import streamlit as st


def show_recommendations(df):

    st.subheader("💡 Smart Business Recommendations")

    # -----------------------------
    # Calculations
    # -----------------------------

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

    best_category = category.idxmax()
    best_category_revenue = category.max()

    best_city = city.idxmax()
    best_city_revenue = city.max()

    top_payment = payment.idxmax()
    payment_count = payment.max()

    top_customer = customer.idxmax()
    top_customer_revenue = customer.max()

    # -----------------------------
    # Cards
    # -----------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.info(
            f"""
### 📈 Category Insight

**Top Category:** {best_category}

**Revenue:** ₹{best_category_revenue:,.0f}

**Recommendation:**
Increase inventory to avoid stock shortages.
"""
        )

    with col2:

        st.info(
            f"""
### 🌍 City Insight

**Top City:** {best_city}

**Revenue:** ₹{best_city_revenue:,.0f}

**Recommendation:**
Increase marketing campaigns in this city.
"""
        )

    col3, col4 = st.columns(2)

    with col3:

        st.info(
            f"""
### 💳 Payment Insight

**Most Used:** {top_payment}

**Orders:** {payment_count}

**Recommendation:**
Offer cashback and payment rewards.
"""
        )

    with col4:

        st.info(
            f"""
### 👤 Customer Insight

**Top Customer:** {top_customer}

**Revenue:** ₹{top_customer_revenue:,.0f}

**Recommendation:**
Launch a VIP loyalty program.
"""
        )