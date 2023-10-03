import streamlit as st
import math

st.set_page_config(page_title="Fabric Calculator", page_icon=":calculator")

st.title("Fabric Calculator")

width = st.number_input("Enter the Window Width :", step=1)
height = st.number_input("Enter the Window Height :", step=1)
panel = math.floor(width / 20)
mam = round((height + 10) / 39 + 0.5, 1)
shm = round((height + 12) / 39 + 0.5, 1)
st.subheader(f"No of Panels : {panel}")
st.subheader(f"Main Material : {mam}")
st.subheader(f"Shear Material : {shm}")

st.write(" ")
st.subheader(f"Total Main Material : {panel * mam}")
st.subheader(f"Total Shear Material : {panel * shm}")

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
