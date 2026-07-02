import streamlit as st

def show_business_insights(df):

    top_city = df.groupby("City")["Revenue"].sum().idxmax()

    top_category = df.groupby("Category")["Revenue"].sum().idxmax()

    top_product = (
        df.groupby("Product")["Quantity"]
        .sum()
        .idxmax()
    )

    average_order_value = df["Revenue"].mean()

    top_payment = (
        df["Payment_Method"]
        .value_counts()
        .idxmax()
    )

    st.subheader("📋 Business Insights")

    insight1, insight2, insight3, insight4, insight5 = st.columns(5)

    with insight1:
        st.info(f"🏆 Top City\n\n{top_city}")

    with insight2:
        st.info(f"💰 Top Category\n\n{top_category}")

    with insight3:
        st.info(f"⭐ Top Product\n\n{top_product}")

    with insight4:
        st.info(f"📈 Avg Order\n\n₹{average_order_value:,.0f}")

    with insight5:
        st.info(f"💳 Top Payment\n\n{top_payment}")