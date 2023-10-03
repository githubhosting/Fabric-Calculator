import streamlit as st
import math
import pandas as pd

st.set_page_config(page_title="Fabric Calculator", page_icon="📏")
st.title("Fabric Calculator Table view")
st.sidebar.header('User Input:')
width = st.sidebar.number_input("Enter the Window Width :", min_value=1, step=1)
height = st.sidebar.number_input("Enter the Window Height :", min_value=1, step=1)
panel = math.floor(width / 20)
mam = f"{((height + 10) / 39 + 0.5):.1f}"
shm = f"{((height + 12) / 39 + 0.5):.1f}"
total_mam = f"{(panel * ((height + 10) / 39 + 0.5)):.1f}"
total_shm = f"{(panel * ((height + 12) / 39 + 0.5)):.1f}"
hide_dataframe_row_index = """
         <style>
         .row_heading.level0 {display:none}
         .blank {display:none}
         </style>
         """
st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)
st.subheader("Calculated Values:")
df = pd.DataFrame(
    {'Calculated Values': ['No of Panels', 'Main Material', 'Shear Material'], 'Values': [panel, mam, shm]})
st.dataframe(df)
st.markdown("---")
st.subheader("Total Material Needed:")
df = pd.DataFrame(
    {'Total Material Needed': ['Total Main Material', 'Total Shear Material'], 'Values': [total_mam, total_shm]})
st.dataframe(df)
