import streamlit as st
import math
from main import name, authentication_status, username, authenticator

st.set_page_config(page_title="Fabric Calculator", page_icon="📏")


def desktop_component():
    st.title("Fabric Calculator")

    st.sidebar.header('User Input:')

    width = st.sidebar.number_input("Enter the Window Width :", min_value=1, step=1)
    height = st.sidebar.number_input("Enter the Window Height :", min_value=1, step=1)

    panel = math.floor(width / 20)
    mam = ((height + 10) / 39 + 0.5)
    shm = ((height + 12) / 39 + 0.5)
    total_mam = panel * mam
    total_shm = panel * shm

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
