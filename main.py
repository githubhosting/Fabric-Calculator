import streamlit as st
import math
import yaml
from streamlit_authenticator import Authenticate
from yaml.loader import SafeLoader

st.set_page_config(page_title="Fabric Calculator", page_icon="📏")

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')


def home():
    st.title("Fabric Calculator")
    # input_type = st.radio("Select Input Type", ("Number", "Slider"), horizontal=True)
    #
    # if input_type == "Slider":
    #     width = st.slider("Enter the Window Width :", min_value=1, max_value=100, step=1)
    #     height = st.slider("Enter the Window Height :", min_value=1, max_value=100, step=1)
    # else:
    width = st.number_input("Enter the Window Width :", min_value=1, step=1)
    height = st.number_input("Enter the Window Height :", min_value=1, step=1)
    panel = math.floor(width / 20)
    mam = (height + 10) / 39 + 0.5
    shm = (height + 12) / 39 + 0.5
    st.subheader(f"No of Panels : {panel}")
    st.subheader(f"Main Material : {mam:.1f}")
    st.subheader(f"Shear Material : {shm:.1f}")

    st.write(" ")
    st.subheader(f"Total Main Material : {panel * mam:.1f}")
    st.subheader(f"Total Shear Material : {panel * shm:.1f}")


if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome {st.session_state["name"]} 👋')
    home()

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
