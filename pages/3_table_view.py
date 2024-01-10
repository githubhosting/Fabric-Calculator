import streamlit as st
import math
import pandas as pd
from main import name, authentication_status, username, authenticator

st.set_page_config(page_title="Fabric Calculator", page_icon="📏")


def calculate_curtains(width, height):
    panel = math.floor(width / 20)
    mam = (height + 10) / 39 + 0.5
    shm = (height + 12) / 39 + 0.5
    track = (width + 12) / 12
    total_mam = panel * mam
    total_shm = panel * shm
    return panel, mam, shm, track, total_mam, total_shm


def calculate_roman_blinds(width, height):
    roman_track = (width + 6) / 12
    blind_stitching = (height + 10) * (width + 10) / 144
    fabric_req = (height + 10) / 39
    total_material_needed = fabric_req if width <= 48 else fabric_req * 2
    return roman_track, blind_stitching, fabric_req, total_material_needed


def calculate_wallpaper(width, height):
    sq_ft = width * height / 144
    no_of_rolls = math.ceil(sq_ft / 50)
    return sq_ft, no_of_rolls


def calculate_custom_blinds(width, height):
    sq_ft = (width + 6) * (height + 12) / 144
    return sq_ft


def table_component():
    st.title("Fabric Calculator Table view")
    st.sidebar.header('User Input:')
    # width = st.sidebar.number_input("Enter the Window Width :", min_value=1, step=1)
    # height = st.sidebar.number_input("Enter the Window Height :", min_value=1, step=1)

    col1, col2 = st.columns(2)

    with col1:
        # Curtain calculations
        panel, mam, shm, track, total_mam, total_shm = calculate_curtains(width, height)
        st.subheader("Curtains")
        curtain_df = pd.DataFrame(
            {'Curtain Values': ['No of Panels', 'Main Material per Panel', 'Shear Material per Panel', 'Track',
                                'Total Main Material', 'Total Shear Material'],
             'Values': [panel, f"{mam:.1f}", f"{shm:.1f}", f"{track:.1f}", f"{total_mam:.1f}", f"{total_shm:.1f}"]})
        # index column should start from 1
        curtain_df.index += 1
        st.dataframe(curtain_df)
        st.markdown("---")

    with col2:
        # Roman Blinds calculations
        roman_track, blind_stitching, fabric_req, total_material_needed = calculate_roman_blinds(width, height)
        st.subheader("Roman Blinds")
        roman_df = pd.DataFrame(
            {'Roman Blind Values': ['Roman Track', 'Blind Stitching', 'Fabric Required/Panel', 'Total Material Needed'],
             'Values': [f"{roman_track:.2f}", f"{blind_stitching:.2f}", f"{fabric_req:.1f}",
                        f"{total_material_needed:.1f}"]})
        roman_df.index += 1
        st.dataframe(roman_df)
        st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        # Wallpaper calculations
        sq_ft, no_of_rolls = calculate_wallpaper(width, height)
        st.subheader("Wallpaper")
        wallpaper_df = pd.DataFrame(
            {'Wallpaper Values': ['SQ Ft', 'No of Rolls'],
             'Values': [f"{sq_ft:.1f}", f"{no_of_rolls}"]})
        wallpaper_df.index += 1
        st.dataframe(wallpaper_df)
        st.markdown("---")

    with col2:
        # Custom Blinds calculations
        custom_sq_ft = calculate_custom_blinds(width, height)
        st.subheader("Custom Blinds")
        custom_df = pd.DataFrame(
            {'Custom Blinds Values': ['SQ Ft'],
             'Values': [f"{custom_sq_ft:.2f}"]})
        custom_df.index += 1
        st.dataframe(custom_df)
        st.markdown("---")


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
                    content:'Developed by Shravan and Team'; 
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
