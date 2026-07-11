import streamlit as st
from datetime import datetime
import requests
import pandas as pd


API_URL = "http://localhost:8000"


def add_analytics_tab():
    col1, col2 = st.columns([1, 1])
    with col1:
        start_date = st.date_input("start date", datetime(2024, 8, 1))
    with col2:
        end_date = st.date_input("end date", datetime(2024, 8, 5))

    if st.button("Analytics"):
        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }
        response = requests.post(f"{API_URL}/analytics/", json=payload)
        response = response.json()
        data = {
            'Category' : list(response.keys()),
            'Total' : [response[category]['total'] for category in response],
            'percentage' : [response[category]['percentage'] for category in response]

        }


        df = pd.DataFrame(data)
        df_sorted = df.sort_values(by="percentage", ascending=False)

        st.title("Expense Tracking By Category")
        st.bar_chart(df_sorted.set_index("Category")["percentage"])
        st.table(df_sorted)




