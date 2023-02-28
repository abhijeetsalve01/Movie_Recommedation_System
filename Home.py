# installing the required libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


# Title
st.title(':red[Netflix] Search System:computer:')
# Description
st.markdown(
    "This project aims to build a movie recommendation mechanism with Netflix Dataset.")

# Netflix JPG
image = Image.open('netflix_logo.jpg')
st.image(image, caption='Neflix')


# hiding the main menu
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

