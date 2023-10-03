import streamlit as st
import math

st.set_page_config(page_title="Fabric Calculator", page_icon="📏")
# Title of the app
st.title("Fabric Calculator")

# Adding a sidebar for inputs
st.sidebar.header('User Input:')

# Getting user input
width = st.sidebar.number_input("Enter the Window Width :", min_value=1, step=1)
height = st.sidebar.number_input("Enter the Window Height :", min_value=1, step=1)

# Calculations
panel = math.floor(width / 20)
mam = ((height + 10) / 39 + 0.5)
shm = ((height + 12) / 39 + 0.5)
total_mam = panel * mam
total_shm = panel * shm

# Displaying Calculated Values
st.subheader("Calculated Values:")
col1, col2 = st.columns(2)

with col1:
    st.markdown("**No of Panels:**")
    st.markdown("**Main Material:**")
    st.markdown("**Shear Material:**")

with col2:
    st.markdown(f"{panel}")
    st.markdown(f"{mam:.1f}")
    st.markdown(f"{shm:.1f}")

st.markdown("---")

st.subheader("Total Material Needed:")
col3, col4 = st.columns(2)

with col3:
    st.markdown("**Total Main Material:**")
    st.markdown("**Total Shear Material:**")

with col4:
    st.markdown(f"{total_mam:.1f}")
    st.markdown(f"{total_shm:.1f}")
