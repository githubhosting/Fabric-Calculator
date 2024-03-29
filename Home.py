import streamlit as st
import math
import yaml
from streamlit_authenticator import Authenticate
# import streamlit_authenticator as stauth
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


def curtain(width, height):
    # st.subheader("Curtain")
    panel = round(width / 20)
    mam = (height + 10) / 39 + 0.5
    shm = (height + 12) / 39 + 0.5
    track = (width + 12) / 12
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(f"No of Panels : :orange[{panel}]")
        st.subheader(f"Main Material per panel (in meters) : :orange[{mam:.1f}]")
        st.subheader(f"Shear Material per panel (in meters) : :orange[{shm:.1f}]")
    with col2:
        st.subheader(f"Total Main Material : :orange[{panel * mam:.1f}]")
        st.subheader(f"Total Shear Material : :orange[{panel * shm:.1f}]")
        st.subheader(f"Track(In Ft) : :orange[{track:.1f}]")


def roman_blind(width, height):
    st.subheader("Minimum order quantity is 15 sft", divider="gray")
    roman_track = (width + 6) / 12
    blind_stitching = (height + 10) * (width + 10) / 144
    fabric_req = (height + 10) / 39
    if width <= 48:
        total_material_needed = fabric_req
    else:
        total_material_needed = fabric_req * 2
    st.subheader(f"Roman Track(In Ft) : :orange[{roman_track:.1f}]")
    st.subheader(f"Blind Stitching(In Ft) : :orange[{blind_stitching:.1f}]")
    st.subheader(f"Fabric Required/Panel : :orange[{fabric_req:.1f}]")
    st.subheader(f"Total Material Needed : :orange[{total_material_needed:.1f}]")


def wallpaper(width, height):
    # st.subheader("Wallpaper")
    sq_ft = width * height / 144
    no_of_rolls = math.ceil(sq_ft / 51)
    st.subheader(f"SQ Ft : :orange[{sq_ft:.1f}]")
    st.subheader(f"No of Rolls : :orange[{no_of_rolls:.1f}]")


def custom_blinds(width, height):
    st.subheader("Minimum order quantity is 15 sft", divider="gray")
    numer = (width + 6) * (height + 12)
    sq_ft = numer / 144
    st.subheader(f"SQ Ft : :orange[{sq_ft:.1f}]")


def home():
    st.image("https://github.com/githubhosting/ds/assets/71520844/941dbaa4-9148-4b01-a089-0dd70c3857bb", width=300)
    st.divider()
    st.subheader("Fabric Calculator",divider="gray")
    st.title("")
    width = st.number_input("Enter the Window Width (in inches):", min_value=1, step=1)
    height = st.number_input("Enter the Window Height (in inches):", min_value=1, step=1)
    tab1, tab2, tab3, tab4 = st.tabs(["Curtain", "Roman Blind", "Wallpaper", "Custom Blinds"])
    with tab1:
        curtain(width, height)

    with tab2:
        roman_blind(width, height)

    with tab3:
        wallpaper(width, height)

    with tab4:
        custom_blinds(width, height)


if st.session_state["authentication_status"]:
    # st.write(f'Welcome {st.session_state["name"]} 👋')
    home()
    st.title("")
    st.divider()
    authenticator.logout('Logout', 'main')

elif not st.session_state["authentication_status"]:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')

hide_streamlit_style = """
                    <style>
                    # MainMenu{
                        visibility: hidden;
                    }
                    footer {
                        visibility: hidden;
                    }
                    footer:after {
                        content:'Developed by Shravan and Team'; 
                        visibility: visible;
                        display: block;
                        position: relative;
                        # background-color: red;
                        padding: 15px;
                        top: 2px;
    	            }
    	            
                    .st-dd{
                        color: #ecbd54 !important;
                    }
                    </style>
                    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
