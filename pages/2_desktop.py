import streamlit as st
import math
from main import name, authentication_status, username, authenticator

st.set_page_config(page_title="Fabric Calculator", page_icon="📏")


def curtains(width, height):
    panel = math.floor(width / 20)
    mam = ((height + 10) / 39 + 0.5)
    shm = ((height + 12) / 39 + 0.5)
    track = (width + 12) / 12
    total_mam = panel * mam
    total_shm = panel * shm

    st.subheader("Curtain Calculations:")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**No of Panels:**")
        st.markdown("**Main Material per Panel (yards):**")
        st.markdown("**Shear Material per Panel (yards):**")
        st.markdown("**Track (In Ft):**")

    with col2:
        st.markdown(f"{panel}")
        st.markdown(f"{mam:.1f}")
        st.markdown(f"{shm:.1f}")
        st.markdown(f"{track:.1f}")

    st.markdown("---")

    st.subheader("Total Material Needed:")
    col3, col4 = st.columns(2)

    with col3:
        st.markdown("**Total Main Material (yards):**")
        st.markdown("**Total Shear Material (yards):**")

    with col4:
        st.markdown(f"{total_mam:.1f}")
        st.markdown(f"{total_shm:.1f}")

    st.markdown("---")


def roman_blind(width, height):
    roman_track = (width + 6) / 12
    blind_stitching = (height + 10) * (width + 10) / 144
    fabric_req = (height + 10) / 39
    if width <= 48:
        total_material_needed = fabric_req
    else:
        total_material_needed = fabric_req * 2

    st.subheader("Roman Blind Calculations:")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Roman Track (In Ft):**")
        st.markdown("**Blind Stitching (In Ft):**")
        st.markdown("**Fabric Required/Panel:**")

    with col2:
        st.markdown(f"{roman_track:.2f}")
        st.markdown(f"{blind_stitching:.2f}")
        st.markdown(f"{fabric_req:.1f}")

    st.markdown("---")

    st.subheader("Total Material Needed:")
    st.markdown(f"**Total Material Needed:** {total_material_needed:.1f}")

    st.markdown("---")


def wallpaper(width, height):
    sq_ft = width * height / 144
    no_of_rolls = math.ceil(sq_ft / 50)

    st.subheader("Wallpaper Calculations:")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**SQ Ft:**")
        st.markdown("**No of Rolls:**")

    with col2:
        st.markdown(f"{sq_ft:.1f}")
        st.markdown(f"{no_of_rolls}")

    st.markdown("---")


def custom_blinds(width, height):
    numer = (width + 6) * (height + 12)
    sq_ft = numer / 144

    st.subheader("Custom Blinds Calculations:")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**SQ Ft:**")

    with col2:
        st.markdown(f"{sq_ft:.2f}")

    st.markdown("---")


def desktop_component():
    st.title("Fabric Calculator")

    st.sidebar.header('User Input:')
    width = st.sidebar.number_input("Enter the Window Width :", min_value=1, step=1)
    height = st.sidebar.number_input("Enter the Window Height :", min_value=1, step=1)

    curtains(width, height)
    roman_blind(width, height)
    wallpaper(width, height)
    custom_blinds(width, height)


if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome {st.session_state["name"]} 👋')
    desktop_component()

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
