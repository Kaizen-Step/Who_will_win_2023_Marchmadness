# Libraries
import streamlit as st
from PIL import Image

# Layout
st.set_page_config(page_title='Who Will Win 2023 March Madness',
                   page_icon=':bar_chart:📈', layout='wide')
st.title(' Conclusion 📑 ')


st.info(""" 
In conclusion, machine learning algorithms (ANN) were used to forecast basketball tournament outcomes. By gathering data on team statistics and the tournament match results, the algorithm was trained to predict the winner of a basketball game with acceptable accuracy. The 18 variables, extracted from official NCAA sites, are run through a sensitivity analysis to determine the most effective variables. It is critical to understand that there is no definitive answer to this question (most effective variables) because this procedure is heavily reliant on trial and error and model characteristics, and the top six variables in the sensevity analysis were chosen as our attempt to find the most effective ones.
We developed a machine-learning algorithm that can predict the result of an NCAA game with 79% accuracy. The results of every game from the 2023 NCAA tournament and the two seasons prior were scraped to generate the new data set, which was then combined into a single table with 1131 match results for each season. The public can use this data collection and it has been posted to Kaggle for future analysis. All 363 teams were rated using six different metrics and characteristics.  The best result weights were extracted and used as initial weights for the 2023 model prediction after the model was first trained using prior season data. The user-interactive application created for all 363 teams in all conferences can show the first team's chances of winning as predicted by the model by choosing the team's opponents and venue situation.Finally, a prediction model was used to predict the March Madness champion and the full bracket.







""")
