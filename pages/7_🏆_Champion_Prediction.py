# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from PIL import Image


# Global Variables
theme_plotly = None  # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday',
             'Thursday', 'Friday', 'Saturday', 'Sunday']

# Layout
st.set_page_config(page_title='Champion - Who Will Win 2023 March Madness',
                   page_icon=':bar_chart:', layout='wide')
st.title('🏆 Who Will Win March Madness 2023')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# SQL Codes
st.write(""" ## Game Prediction on Bracket ## """)

st.write("""
As of March 24, most of the games are finished, so the most recent bracket is downloaded from the CBS official website. The remaining games have been predicted with the upgraded model. However, the predicted champion is still Houston, beating Alabama in the finals.



""")

st.text(" \n")

st.image(Image.open('Images/charts.jpg'))
