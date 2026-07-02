import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression


def show_ai_forecast(df):
    st.title("🤖 AI Sales Forecast")

    forecast_period = st.selectbox(
        "📅 Forecast Period",
        [1, 3, 6, 12],
        index=0
    )

    monthly_sales = (
        df.groupby(df["Order_Date"].dt.to_period("M"))["Revenue"]
        .sum()
        .reset_index()
    )

    monthly_sales["Month_Number"] = range(1, len(monthly_sales) + 1)
    monthly_sales["Order_Date"] = monthly_sales["Order_Date"].astype(str)

    X = monthly_sales[["Month_Number"]]
    y = monthly_sales["Revenue"]

    model = LinearRegression()
    model.fit(X, y)

    future_months = list(
        range(
            len(monthly_sales) + 1,
            len(monthly_sales) + forecast_period + 1
        )
    )

    future_df = pd.DataFrame(
        {"Month_Number": future_months}
    )

    predictions = model.predict(future_df)

    future_df["Revenue"] = predictions
    future_df["Order_Date"] = [
        f"Month +{i}"
        for i in range(1, forecast_period + 1)
    ]

    last_revenue = monthly_sales["Revenue"].iloc[-1]

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "📈 Next Month Revenue",
            f"₹{predictions[0]:,.0f}"
        )

    growth = (
        (predictions[0] - last_revenue)
        / last_revenue
    ) * 100

    with col2:
        st.metric(
            "📊 Predicted Growth",
            f"{growth:.2f}%"
        )

    st.divider()

    chart_df = pd.concat(
        [
            monthly_sales[["Order_Date", "Revenue"]],
            future_df[["Order_Date", "Revenue"]]
        ],
        ignore_index=True
    )

    fig = px.line(
        chart_df,
        x="Order_Date",
        y="Revenue",
        markers=True,
        title="Revenue Forecast"
    )

    st.plotly_chart(fig, width="stretch")