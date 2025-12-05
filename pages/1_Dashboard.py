import streamlit as st
import pandas as pd
from APP.db import get_connection
from APP.metadeta import get_all_datasets_metadata
from APP.tickets import get_all_it_tickets
from APP.incidents import get_all_cyber_incidents

conn = get_connection()

st.set_page_config(
    page_title="Dashboard",
    page_icon=":dolphin:",
    layout="wide",
)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.error("Please log in to access the dashboard.")

    if st.button("Go to Home"):
        st.session_state.logged_in = False
        st.switch_page("Home.py")
    st.stop()

datasets = pd.DataFrame(get_all_datasets_metadata(conn))
cyber = pd.DataFrame(get_all_cyber_incidents(conn))
tickets = pd.DataFrame(get_all_it_tickets(conn))
st.title("DASHBOARD")
st.subheader("Overview of Data")

def temp():
    with st.expander("Datasets Metadata"):
        st.write("Raw data:")
        st.dataframe(datasets)
def temp():
    with st.expander("IT Tickets"):
        st.write("Raw data:")
        st.dataframe(tickets)

with st.expander("Cyber Incidents"):
    st.write("Raw data:")
    st.dataframe(cyber)

with st.sidebar:
    st.header("Navigation")
    severity = st.selectbox("Severity", cyber["severity"].unique())

cyber["timestamp"] = pd.to_datetime(cyber["timestamp"])
filtered_cyber = cyber[cyber["severity"] == severity]

col1, col2 = st.columns(2)

with col1:
    st.bar_chart(filtered_cyber["category"].value_counts())
with col2:
    st.line_chart(filtered_cyber["timestamp"])

st.dataframe(filtered_cyber)



def temp_col():
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("silly goober ------>")
    with col2:
        st.image("https://i.pinimg.com/736x/46/50/51/465051466fccf326ac202364300d5f02.jpg")



