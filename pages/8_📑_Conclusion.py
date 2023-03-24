# Libraries
import streamlit as st
from PIL import Image

# Layout
st.set_page_config(page_title='Insight of the Week',
                   page_icon=':bar_chart:📈', layout='wide')
st.title(' Conclusion 📑 ')

st.info(""" 
In conclusion, machine learning algorithms (ANN) were used to forecast basketball tournament outcomes. By gathering data on team statistics and the tournament match results, the algorithm was trained to predict the winner of a basketball game with high accuracy. The 18 variables, extracted from official NCAA sites, are run through a sensitivity analysis to determine the most effective variables. It is important to know that, there is no definitive answer to this question because this procedure relies heavily on trial and error and model characteristics, and the sensevity analysis's top six variables were selected are our attempt to find the most effective ones.
We developed a machine learning model that can predict the NCAA match result with 78% accuracy, which is a good result that shows the possibility of using ANN in this concept. The new data set was created by scraping 2023 NCAA teams for each individual game and gathered up in one table with 1131 match results with details. This document was uploaded on Kaggle for future investigation and public usage. The overall 363 team was evaluated by 8 different features and statistics, and the one predicted by the ANN tensor flow model had the best chance of winning. the user-interactive application created for all 363 teams in all different conferences to show the result by choosing the two teams and team number one venue. The model predicts the probability of winning for the first team.


""")
