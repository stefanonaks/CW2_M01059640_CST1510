import streamlit as st
import pandas as pd
from APP.db import conn
from APP.metadeta import get_all_datasets_metadata
from APP.tickets import get_all_it_tickets
from APP.incidents import get_all_cyber_incidents

st.set_page_config(
    page_title="My App",
    page_icon=":dolphin:",
    layout="wide",
)

df = get_all_datasets_metadata()
data = pd.DataFrame(df)

st.title("DASHBOARD")
with st.expander("Datasets Metadata"):
    st.write("Raw data:")
    st.dataframe(data)


col1, col2 = st.columns(2)
with col1:
    st.subheader("silly goober ------>")
with col2:
    st.image("https://i.pinimg.com/736x/46/50/51/465051466fccf326ac202364300d5f02.jpg")