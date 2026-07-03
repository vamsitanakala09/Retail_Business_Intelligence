import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression


def show_ai_forecast(df):
    st.title("🤖 AI Sales Forecast")

    forecast_period = st.selectbox(
        "📅 Forecast Period (Months)",
        [1, 3, 6, 12],
        index=0
    )

    # Monthly Revenue
    monthly_sales = (
        df.groupby(df["Order_Date"].dt.to_period("M"))["Revenue"]
        .sum()
        .reset_index()
    )

    monthly_sales["Month_Number"] = range(1, len(monthly_sales) + 1)
    monthly_sales["Order_Date"] = monthly_sales["Order_Date"].dt.to_timestamp()

    # Train Model
    X = monthly_sales[["Month_Number"]]
    y = monthly_sales["Revenue"]

    model = LinearRegression()
    model.fit(X, y)

    # Future Months
    future_months = range(
        len(monthly_sales) + 1,
        len(monthly_sales) + forecast_period + 1
    )

    future_df = pd.DataFrame({
        "Month_Number": future_months
    })

    future_df["Revenue"] = model.predict(future_df)

    last_date = monthly_sales["Order_Date"].max()

    future_df["Order_Date"] = pd.date_range(
        start=last_date + pd.DateOffset(months=1),
        periods=forecast_period,
        freq="MS"
    )

    # ---------------- KPI Cards ---------------- #

    last_revenue = monthly_sales["Revenue"].iloc[-1]
    predicted_revenue = future_df["Revenue"].iloc[-1]

    growth = (
        (predicted_revenue - last_revenue)
        / last_revenue
    ) * 100

    total_forecast = future_df["Revenue"].sum()
    avg_forecast = future_df["Revenue"].mean()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "💰 Forecast Revenue",
        f"₹{predicted_revenue:,.0f}"
    )

    col2.metric(
        "📈 Growth",
        f"{growth:.2f}%"
    )

    col3.metric(
        "📊 Avg Forecast",
        f"₹{avg_forecast:,.0f}"
    )

    col4.metric(
        "💵 Total Forecast",
        f"₹{total_forecast:,.0f}"
    )

    st.divider()

    # Historical + Forecast
    monthly_sales["Type"] = "Historical"
    future_df["Type"] = "Forecast"

    chart_df = pd.concat(
        [
            monthly_sales[["Order_Date", "Revenue", "Type"]],
            future_df[["Order_Date", "Revenue", "Type"]]
        ],
        ignore_index=True
    )

    fig = px.line(
        chart_df,
        x="Order_Date",
        y="Revenue",
        color="Type",
        line_dash="Type",
        markers=True,
        title="Historical vs Forecast Revenue"
    )

    fig.update_layout(
        xaxis_title="Month",
        yaxis_title="Revenue",
        legend_title="Data",
        hovermode="x unified"
    )

    st.plotly_chart(fig, width="stretch")

    st.subheader("📅 Forecast Details")

    forecast_table = future_df.copy()

    forecast_table["Month"] = forecast_table[
        "Order_Date"
    ].dt.strftime("%b %Y")

    forecast_table["Predicted Revenue"] = forecast_table[
        "Revenue"
    ].round(2)

    st.dataframe(
        forecast_table[
            ["Month", "Predicted Revenue"]
        ],
        width="stretch"
    )
    csv = forecast_table[
        ["Month", "Predicted Revenue"]
    ].to_csv(index=False)

    st.download_button(
        label="📥 Download Forecast CSV",
        data=csv,
        file_name="RetailIQ_Sales_Forecast.csv",
        mime="text/csv"
    )

    st.divider()

    highest = forecast_table.loc[
        forecast_table["Revenue"].idxmax()
    ]

    lowest = forecast_table.loc[
        forecast_table["Revenue"].idxmin()
    ]

    trend = (
        "Increasing 📈"
        if growth > 0
        else "Decreasing 📉"
    )

    st.subheader("🧠 AI Forecast Insights")

    st.success(
        f"""
• Expected Trend: **{trend}**

• Highest Forecast Revenue:
₹{highest['Revenue']:,.0f}
({highest['Month']})

• Lowest Forecast Revenue:
₹{lowest['Revenue']:,.0f}
({lowest['Month']})

• Average Monthly Forecast:
₹{avg_forecast:,.0f}

• Total Forecast Revenue:
₹{total_forecast:,.0f}
"""
    )