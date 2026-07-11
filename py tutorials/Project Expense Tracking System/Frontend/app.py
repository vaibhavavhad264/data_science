"""
import datetime

import streamlit as st
import pandas as pd

# # test element
# st.header("Streamlit Core Feature")
# st.subheader("Test Element")
# st.text("This is the simple test element")
#
# # Data display
#
# st.subheader("Data Display")
# st.write("Here is simple table")
#
# df = pd.DataFrame({
#     "Date" : ["2024-08-01", "2024-09-01", "2024-10-01", "2024-11-01", "2024-12-01"],
#     "Amount" : [250, 490, 560, 780, 999]
# })
#
# st.table(df)
#
# #charts
#
# st.subheader("Charts")
# st.line_chart(df["Amount"])
#
# #User Input
# st.subheader("User Input")
# value = st.slider("Select a value", 0, 100)
# st.write("Your Selected Value Is : ", value)
#
#

# st.title("Interactive Widget Example")
#
# if st.checkbox("SHOW/HIDE"):
#     st.write("Checkbox is checked")
#
# option = st.selectbox("Select a number", [1, 2, 3, 4])
# st.write(f" You Selected {option}")
#
# options = st.multiselect("Select an option", [1, 2, 3, 4])
# st.write(f" You Selected {options}")

"""
import streamlit as st
from updated_ui import add_update_tab
from analytics import add_analytics_tab



st.title("Expense Tracking System")

tab1, tab2 = st.tabs(["Add/Update", "Analytics"])

with tab1:
    add_update_tab()

with tab2:
    add_analytics_tab()









