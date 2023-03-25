import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import pickle
from PIL import Image
# Theme
theme_plotly = None  # None or streamlit

# Layout
st.set_page_config(page_title=' Model - Who Will Win 2023 March Madness',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('🌌 Optimized Model')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache_data()
def get_data(query):
    # if query == 'Total_Genre':
    #     return pd.read_csv('https://raw.githubusercontent.com/Kaizen-Step/Hollywood_Box_Office_Tragedy/main/Data/Geners/Genre-Total.csv')
    # elif query == 'Number_of_Release':
    #     return pd.read_csv('https://raw.githubusercontent.com/Kaizen-Step/Hollywood_Box_Office_Tragedy/main/Data/Geners/Genre-Total2.csv')
    # elif query == 'average_per_release':
    #     return pd.read_csv('https://raw.githubusercontent.com/Kaizen-Step/Hollywood_Box_Office_Tragedy/main/Data/Geners/Genre-Total3.csv')
    return None


Total_Genre = get_data('Total_Genre')
Number_of_Release = get_data('Number_of_Release')
average_per_release = get_data('average_per_release')


df = Total_Genre
df2 = Number_of_Release
df3 = average_per_release
##########################################################################
st.write(""" ### Machine Learning Model  ##  """)

st.write("""
  Machine learning can be used to predict the outcome of basketball matches by training a model on historical data of past games. The model can analyze various factors such as team rankings, player statistics, and game conditions to identify patterns that may influence the game's result.
The process of creating a basketball prediction model involves:     
* Collecting data: Gathering data on past basketball games, including team rankings, player statistics, and game conditions  
* Preprocessing data: Cleaning and preparing the data for analysis by handling missing values and converting it into a suitable format  
* Feature engineering: Identifying the relevant features that can be used to train the model and engineering new features based on domain knowledge  
* Model selection: Choosing an appropriate machine learning algorithm, such as decision trees, support vector machines, or neural networks, to train the model  
* Training: Feeding the data into the chosen model and adjusting its parameters to optimize its performance  
* Evaluation: Testing the model's performance on a separate set of data to assess its accuracy and generalization ability  
* Deployment: Integrating the trained model into a larger system or application, where it can be used to make predictions on new basketball matches  
  """)


st.info(""" ##### In This Model Section you can find: ####    

 
    * Model Features
    * Training The Model With Past Season Data
    * Use Pretrained Model to Develop More Accurate Model
    * Future Plan
    
    """)
#################################################################################################
st.write(""" ### Model Features ##  """)

st.write("""
The five neurons in the neural network that is being used have a 20% dropout rate. As we only have a limited set of data, the model can't be too complex to prevent overfitting. You can observe accuracy and loss values over the course of training in the following charts. The training and validation sets both reach acceptable values. In the test dataset set, the prediction came in at almost 75%, which seems reasonable.
  """)

st.write(""" ### Training The Model With Past Season Data ##  """)

st.write("""  


This project has made use of the dataset that was obtained through scraping. The dataset has a total of 38 input. A sensitivity analysis and some trial-and-error were used to eliminate some of the columns that were less useful than others. The remaining columns (features) are: "RK1", "Win_Rate1" "offensive rebound rate allowed1," "adjusted offensive efficiency1," "Barthag1," "turnover percentage committed1," "adjusted defensive efficiency1," "RK2," " Win_Rate2," "offensive rebound rate allowed2," "adjusted offensive efficiency2," "Barthag2," "turnover percentage committed2," "adjusted defensive efficiency2", Venue_Home, Venue_Away, and Venue_Neutral.
Win_Rate1 and Win_Rate2 are representations of the number of victories divided by the total number of games played by each squad.The other characteristics were taken from the Barttorvik website. For a hidden layer and an output layer, respectively, the relu and sigmoid activation functions demonstrated the highest degree of precision.
  """)

st.info(""" ##### Using a Larger Dataset (two consecutive seasons data) ####    

    The data from the prior season (both regular season and playoff) was used in this project, as opposed to the previous project, which only used the 2023 regular season dataset to train the model.   
    Two criteria were utilized.:
    
    * Concatenate all the data and train the model on the larger dataset altogether
    * Use the 2021-22 data to pre-train the model, then, load the weights as initial values and then train the model again with the current season data

    The result showed that the second option works better, therefore, the model is trained by using all the games of current season as a whole dataset.

    The interesting result is that the accuracy on the test dataset increased by more than half percent by training the model on this approach. The accuracy increased from 76.66 to 78.18 percent. The final accuracy on the test set is just below 80 percent, which looks quite satisfying.
    
    """)


st.write("""
The following charts display the accuracy and loss values while training on both datasets. Please note that since the y axis limit in a bit smaller on the below charts, it seems that it has more flucuations; however, both cases seem to have converged.
  """)

# load
with open('Data/Prediction/Model History_only_2022/trainHistoryDict', "rb") as file_pi:
    history_1 = pickle.load(file_pi)


c1, c2 = st.columns(2)

with c1:
    # Plot accuracy
    st.write(" ### Accuracy - Trained on 2021-22 Dataset")
    fig = go.Figure()

    for accuracy in [history_1['accuracy'], history_1['val_accuracy']]:
        fig = fig.add_trace(go.Scatter(y=accuracy))

    fig.update_layout(legend_title=None, xaxis_title='Epoch',
                      yaxis_title='Accuracy')

    st.plotly_chart(fig)

with c2:
    # Plot loss
    st.write(" ### Loss - Trained on 2021-22 Dataset")
    fig = go.Figure()

    for loss in [history_1['loss'], history_1['val_loss']]:

        fig = fig.add_trace(go.Scatter(y=loss))

    fig.update_layout(legend_title=None, xaxis_title='Epoch',
                      yaxis_title='Loss')

    st.plotly_chart(fig)

# load
with open('Data/Prediction/Model History_concat_data/trainHistoryDict', "rb") as file_pi:
    history_2 = pickle.load(file_pi)


c1, c2 = st.columns(2)

with c1:
    # Plot accuracy
    st.write(" ### Accuracy - Trained on the Whole Dataset (2021-22 season and the Regular Season of 2022-23)")
    fig = go.Figure()

    for accuracy in [history_2['accuracy'], history_2['val_accuracy']]:
        fig = fig.add_trace(go.Scatter(y=accuracy))

    fig.update_layout(legend_title=None, xaxis_title='Epoch',
                      yaxis_title='Accuracy')

    st.plotly_chart(fig)

with c2:
    # Plot loss
    st.write(" ### Loss - Trained on the Whole Dataset (2021-22 season and the Regular Season of 2022-23)")
    fig = go.Figure()

    for loss in [history_2['loss'], history_2['val_loss']]:

        fig = fig.add_trace(go.Scatter(y=loss))

    fig.update_layout(legend_title=None, xaxis_title='Epoch',
                      yaxis_title='Loss')

    st.plotly_chart(fig)


st.write("""  By brute forcing various hyper-parameters for the deep neural model, the best choices are selected. In the charts below, two of the models with the best results are displayed. In both cases the accuracy on the validation set is about 75 percent, but the noticeable problem is that there is a significant difference between the accuracy of the training set and the validation set. Moreover, they do not seem to diverge, and the model, even with a bigger dataset, still can easily overfit with a deeper neural network. So the most promising model would have a single hidden layer that consists of 5 neurons and a dropout rate of 20 percent.	 """)

st.write(" ### Neural Network Model With Two Hidden Layers (n1=128, n2=16, dropout=0.3)")
c1, c2 = st.columns(2)
with c1:
    st.image(Image.open('Images/acc - two layers.png'), )
with c2:
    st.image(Image.open(
        'Images/loss - two layers.png'), )


st.write(" ### Neural Network Model With Three Hidden Layers (n1=64, n2=16, n3=16, dropout=0.3)")
c1, c2 = st.columns(2)
with c1:
    st.image(Image.open('Images/acc - three layers.png'), )
with c2:
    st.image(Image.open(
        'Images/loss - three layers.png'), )


#####################################################

st.write(""" ### Future Plan ##  """)


st.write("""  In the future, other results of other models such as linear regression or random forest can be investigated and compared with the current model. In addition, deeper models still can be investigated in more depth, so that a method can be used to prevent model from overfitting, even though there is a lack of data. One solution could be extracting more data from the previous seasons. """)
