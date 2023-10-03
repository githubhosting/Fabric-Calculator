import streamlit as st

st.set_page_config(page_title="Fabric Calculator", page_icon="")

st.title("Fabric Calculator")

st.write(
    "This is a AI based meal planner that uses a persons information. The planner can be used to find a meal plan that satisfies the user's calorie and macronutrient requirements.")

st.write("Enter your information:")
name = st.text_input("Enter your name")
age = st.number_input("Enter your age", step=1)
weight = st.number_input("Enter your weight (kg)")
height = st.number_input("Enter your height (cm)")
gender = st.radio("Choose your gender:", ["Male", "Female"])
st.subheader(f"Your daily intake needs to have:  calories")

if 'clicked' not in st.session_state:
    st.session_state.clicked = False


def click_button():
    st.session_state.clicked = True


st.button("Create a Basket", on_click=click_button)
if st.session_state.clicked:
    st.write("You clicked the button")
    st.session_state.clicked = False

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
