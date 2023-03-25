# Libraries
import streamlit as st
from PIL import Image

# Layout
st.set_page_config(page_title=' Who Will Win 2023 March Madness',
                   page_icon=':bar_chart:📈', layout='wide')
st.title(' Who Will Win 2023 March Madness? 🏀')
st.text(" \n")
# Content
c1, c2, c3 = st.columns(3)


with c1:
    st.text(" \n")
    st.text(" \n")
    st.image(Image.open('Images/wni1.jpg'))

with c2:
    st.text(" \n")
    st.text(" \n")
    st.image(Image.open('Images/win7.jpg'))
with c3:
    st.text(" \n")
    st.text(" \n")
    st.image(Image.open('Images/win8.jpg'))


st.write("""
### NCAA March Madness tournament ###
The NCAA Division I men's basketball tournament, branded as NCAA March Madness and commonly called March Madness, is a single-elimination tournament played each spring in the United States, currently featuring 68 college basketball teams from the Division I level of the National Collegiate Athletic Association (NCAA), to determine the national champion. The tournament was created in 1939 by the National Association of Basketball Coaches, and was the idea of Ohio State coach Harold Olsen. Played mostly during March, it has become one of the most popular annual sporting events in the United States.   
The tournament teams include champions from 32 Division I conferences (which receive automatic bids), and 36 teams which are awarded at-large berths. These "at-large" teams are chosen by an NCAA selection committee, then announced in a nationally televised event dubbed Selection Sunday. The 68 teams are divided into four regions and organized into a single-elimination "bracket", which pre-determines – when a team wins a game – which team it will face next. Each team is "seeded", or ranked, within its region from 1 to 16. After the First Four round, the remainder of the tournament begins the third Thursday of March, and is played over the course of three weekends, at pre-selected neutral sites across the United States. Teams, seeded by rank, proceed through a single-game elimination bracket beginning with the First Four round, a first round consisting of 64 teams playing in 32 games over the course of two days, the second round consisting of the 32 remaining teams playing in 16 games that weekend, the "Sweet Sixteen" and "Elite Eight" rounds the next week and weekend, respectively, and – for the last weekend of the tournament – the "Final Four" round. The two Final Four games are played the Saturday preceding the first Sunday in April, with the championship game on Monday. These four teams, one from each region (East, South, Midwest, and West), compete in a preselected location for the national championship.[[1]](https://en.wikipedia.org/wiki/NCAA_Division_I_men%27s_basketball_tournament) """)

st.write("""
### March Madness Winner Prediction with Machine Learning Algorithms ###
The term ‘machine learning’ is often, incorrectly, interchanged with Artificial Intelligence, but machine learning is actually a sub
field/type of AI. Machine learning is also often referred to as predictive analytics, or predictive modelling.
Coined by American computer scientist Arthur Samuel in 1959, the term ‘machine learning’ is defined as a “computer’s ability to learn without being explicitly programmed”.
At its most basic, machine learning uses programmed algorithms that receive and analyse input data to predict output values within an acceptable range. As new data is fed to these algorithms, they learn and optimise their operations to improve performance, developing ‘intelligence’ over time.
There are four types of machine learning algorithms: supervised, semi-supervised, unsupervised and reinforcement.  
n supervised learning, the machine is taught by example. The operator provides the machine learning algorithm with a known dataset that includes desired inputs and outputs, and the algorithm must find a method to determine how to arrive at those inputs and outputs. While the operator knows the correct answers to the problem, the algorithm identifies patterns in data, learns from observations and makes predictions. The algorithm makes predictions and is corrected by the operator – and this process continues until the algorithm achieves a high level of accuracy/performance.[[2]](https://www.sas.com/en_gb/insights/articles/analytics/machine-learning-algorithms.html#:~:text=At%20its%20most%20basic%2C%20machine,developing%20'intelligence'%20over%20time.  ) """)


st.write("""
## Methodology ##   
March Madness is one of the most exciting times of the year for college basketball fans. Every year, millions of people try to predict the winner of the NCAA tournament, but the truth is that it's extremely difficult to do so accurately. With the help of machine learning algorithms, it's possible to analyze vast amounts of data and make more informed predictions. In order to do this, we gathered match results for 2022–2023 as well as data from previous seasons. All of the match result data used in this dashboard was scraped from the [NCAA](https://www.ncaa.org), [Barttorvik](https://barttorvik.com) and [Kepnom](https://kenpom.com) sites which combined into a single data set, and shared with the public on [Kaggle-kaizenstep-ncaa-games-results](https://www.kaggle.com/datasets/kaizenstep/ncaa-2023-all-games-results).
One of the most important factors in predicting the winner of March Madness is analyzing the teams' performances. This can include their records throughout the season, their strength of schedule, and win rate. However, this is just the tip of the iceberg when it comes to the types of data that can be analysed, as we gathered 18 individual variables that might have influenced the match winner from Barttorvik and Kepnom sites. then run these 18 variables through a sensivity analysis to determine the most effective variables. These effective variables were used to develop a prediction model that could forecast a team's chances of winning by picking its opponents and playing in venue situation.
 In order to increase the precision of the prediction model for the match results in 2023, weights generated from models built with the previous tournament data were used as initial weights for the 2023 model. The user-interactive application provided can instantly predict a team's chances of winning in real time. Finally, the game for March Madness 2023 was predicted all the way to the championship, and the winning team was shown on the bracket. A glossary section is provided that contains the definition and formula of each variable and the statistics used in this dashboard.
""")


st.text(" \n")
st.write("""   
#### Sources ####  """)
st.write("""    1.https://www.ncaa.org/news/2022/3/10/media-center-from-authorized-sources.aspx     
                2.https://www.sas.com/en_gb/insights/articles/analytics/machine-learning-algorithms.html#:~:text=At%20its%20most%20basic%2C%20machine,developing%20'intelligence'%20over%20time.  
        3.https://www.bannersontheparkway.com/2023/2/13/23598002/rule-15-2-a-and-the-state-of-officials-in-college-basketball-big-east    
        4.https://kenpom.com/    
        5.https://barttorvik.com/trank.php#  
            """)


st.text(" \n")
c1, c2 = st.columns(2)
with c1:
    st.info(
        '**Twitter:  [Ludwig.1989](https://flipsidecrypto.xyz/)**', icon="🕊️")
    st.info(
        '**Data Set (1):  [Our own upploaded Data Set Match Results (Kaggle)](https://www.kaggle.com/datasets/kaizenstep/ncaa-2023-all-games-results)**', icon="🧠")

with c2:
    st.info(
        '**Project Github:  [Who Will Win 2023 March Madness](https://github.com/Kaizen-Step/Who_will_win_2023_Marchmadness)**', icon="💻")
    st.info(
        '**Data Set (2):  [Barttorvik](https://barttorvik.com/trank.php#)**', icon="🧠")
