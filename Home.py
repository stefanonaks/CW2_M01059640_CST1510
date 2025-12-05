import streamlit as st
from APP.db import get_connection
from APP.users import hash_password, validate_password, add_user, get_user
conn = get_connection()
st.set_page_config(
    page_title="Home",
    page_icon=":dolphin:",
    layout="wide",
)

st.title("HOME PAGE")
st.write("Welcome. Use the sidebar to navigate through the app.")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

tab_login, tab_register = st.tabs(["Login", "Register"])

with tab_login:
    st.subheader("Login")
    login_username = st.text_input("Username")
    login_password = st.text_input("Password", type="password")

    if st.button("Login"):
        id, name, hashed_password, role = get_user(conn, login_username)
        if login_username == name and validate_password(login_password, hashed_password):
            st.session_state.logged_in = True
            st.success("Logged in successfully!")
            st.switch_page("pages/1_Dashboard.py")

with tab_register:
    st.subheader("Register")
    register_username = st.text_input("New Username")
    register_password = st.text_input("New Password", type="password")

    if st.button("Register"):
        hashed_password = hash_password(register_password)
        add_user(conn, register_username, hashed_password)
        st.success("Registered successfully! You can now log in.")

st.session_state