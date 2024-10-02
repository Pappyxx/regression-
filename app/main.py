#streamlit web file

import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
    page_title="predictprice"
)

with st.sidebar:
    selected = option_menu(
        menu_title = None,
        options = ["Home","prediction","Dashbord"],
        icons =["home","",""],
        menu_icon ="cast",
        default_index = 0
    )