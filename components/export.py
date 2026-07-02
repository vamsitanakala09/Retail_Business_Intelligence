import pandas as pd
from io import BytesIO
import streamlit as st


def download_excel(df):

    output = BytesIO()

    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="RetailIQ")

    excel_data = output.getvalue()

    st.download_button(
        label="📄 Download Excel Report",
        data=excel_data,
        file_name="RetailIQ_Report.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )