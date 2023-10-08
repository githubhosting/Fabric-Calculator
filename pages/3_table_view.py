import streamlit as st
import math
import pandas as pd
from main import name, authentication_status, username, authenticator

st.set_page_config(page_title="Fabric Calculator", page_icon="📏")


def table_component():
    st.title("Fabric Calculator Table view")
    st.sidebar.header('User Input:')
    width = st.sidebar.number_input("Enter the Window Width :", min_value=1, step=1)
    height = st.sidebar.number_input("Enter the Window Height :", min_value=1, step=1)
    panel = math.floor(width / 20)
    mam = f"{((height + 10) / 39 + 0.5):.1f}"
    shm = f"{((height + 12) / 39 + 0.5):.1f}"
    total_mam = f"{(panel * ((height + 10) / 39 + 0.5)):.1f}"
    total_shm = f"{(panel * ((height + 12) / 39 + 0.5)):.1f}"
    mam = float(mam)
    shm = float(shm)
    total_mam = float(total_mam)
    total_shm = float(total_shm)
    st.subheader("Calculated Values:")
    df = pd.DataFrame(
        {'Calculated Values': ['No of Panels', 'Main Material', 'Shear Material'], 'Values': [panel, mam, shm]})
    st.dataframe(df)
    st.markdown("---")
    st.subheader("Total Material Needed:")
    df = pd.DataFrame(
        {'Total Material Needed': ['Total Main Material', 'Total Shear Material'], 'Values': [total_mam, total_shm]})
    st.dataframe(df)


if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome {st.session_state["name"]} 👋')
    table_component()

elif not st.session_state["authentication_status"]:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')

hide_streamlit_style = """
                    <style>
                    # MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    footer:after {
                    content:'Made with Passion by Shravan and Team'; 
                    visibility: visible;
    	            display: block;
    	            position: relative;
    	            # background-color: red;
    	            padding: 15px;
    	            top: 2px;
    	            }
                    </style>
                    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
