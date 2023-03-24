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
st.set_page_config(page_title='Glossary - Who will win 2023 March Madness',
                   page_icon=':bar_chart:', layout='wide')
st.title('📜 Glossary')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.write(""" ### Basketball Statistics Glossary ##  """)

st.write("""
  The glossary section provides definitions of key terms and phrases used in the dashboard. It helps users to better understand the terminology and concepts used in the dashboard, which can be helpful in making informed decisions when predicting NCAA match outcomes. The glossary include explanations of statistical measures, performance metrics, and other relevant terms related to college basketball and NCAA match prediction.

  """)


st.info(""" ##### In This Glossary section you can find: ####   

* Adjusted Offensive Efficiency  
* Effective Field Goal Percentage Shot    
* Turnover Percentage Committed (Steal Rate)
* Offensive Rebound Rate  
* Free Throw Rate (How often the given team shoots Free Throws)  
* Two-Point Shooting Percentage   
* Three-Point Shooting Percentage    
* Wins Above Bubble
* ADJDE: Adjusted Defensive Efficiency 
* ADJ_T: Adjusted Tempo       
* EFG_D: Effective Field Goal Percentage Allowed  
* TOR: Turnover Percentage Allowed (Turnover Rate)  
* DRB: Offensive Rebound Rate Allowed   
* FTRD: Free Throw Rate Allowed   
* 2P_D: Two-Point Shooting Percentage Allowed      
* 3P_D: Three-Point Shooting Percentage Allowed  
        """)

###############################################################################################

st.write(""" ### Adjusted Offensive Efficiency [ADJOE] ##  """)

st.write(""" Adjusted Offensive Efficiency (AOE) is a basketball statistic that measures how effectively a team scores points per possession, while accounting for the strength of the opposing team's defense. AOE is typically calculated by taking a team's points scored per 100 possessions and adjusting that number based on the strength of the opposing team's defense, as well as the pace of the game.
One commonly used method for calculating AOE is to use the formula:      

  AOE = (Points Scored / Possessions) * (League Average Efficiency / Opponent's Defensive Efficiency)     
  
By adjusting for the strength of the opposing team's defense and the pace of the game, AOE provides a more accurate measure of a team's offensive performance than simply looking at their raw points scored per game.
   

  """)

##############################################################
st.write(""" ### Effective Field Goal Percentage Shot [EFG_O] ##  """)

st.write(""" Effective Field Goal Percentage (eFG%) is a basketball statistic that measures a player's shooting efficiency. It is a modification of the traditional Field Goal Percentage (FG%), which only takes into account two-point field goals and three-point field goals.
In contrast, eFG% takes into account the fact that three-point field goals are worth more than two-point field goals. The formula for eFG% is:  

eFG% = (FGM + 0.5 * 3PM) / FGA  

where FGM is the number of field goals made, 3PM is the number of three-point field goals made, and FGA is the number of field goal attempts.  
By adding 0.5 times the number of three-pointers made to the number of two-pointers made in the numerator, eFG% effectively weights three-pointers as if they were 1.5 two-pointers. This provides a more accurate picture of a player's shooting efficiency and helps to compare players who shoot a different mix of two-pointers and three-pointers.  
eFG% is particularly useful for evaluating players who are efficient at shooting three-pointers. For example, a player who shoots 50% on two-point field goals and 33% on three-point field goals would have a FG% of 43.3%, which is below average. However, their eFG% would be 51.7%, which is above average because their three-pointers are weighted more heavily.   
   

  """)


############################################################
st.write(""" ### Effective Field Goal Percentage Shot [EFG_O] ##  """)

st.write(""" Effective Field Goal Percentage (eFG%) is a basketball statistic that measures a player's shooting efficiency. It is a modification of the traditional Field Goal Percentage (FG%), which only takes into account two-point field goals and three-point field goals.
In contrast, eFG% takes into account the fact that three-point field goals are worth more than two-point field goals. The formula for eFG% is:  

eFG% = (FGM + 0.5 * 3PM) / FGA  

where FGM is the number of field goals made, 3PM is the number of three-point field goals made, and FGA is the number of field goal attempts.  
By adding 0.5 times the number of three-pointers made to the number of two-pointers made in the numerator, eFG% effectively weights three-pointers as if they were 1.5 two-pointers. This provides a more accurate picture of a player's shooting efficiency and helps to compare players who shoot a different mix of two-pointers and three-pointers.  
eFG% is particularly useful for evaluating players who are efficient at shooting three-pointers. For example, a player who shoots 50% on two-point field goals and 33% on three-point field goals would have a FG% of 43.3%, which is below average. However, their eFG% would be 51.7%, which is above average because their three-pointers are weighted more heavily.   
   

  """)


######################################################

st.write(""" ### Offensive Rebound Rate [ORB] """)

st.write(""" Offensive Rebound Rate (ORR) is a statistic used in basketball to measure the percentage of missed shots by a team that are rebounded by that same team. Specifically, it is the number of offensive rebounds divided by the total number of missed field goals and missed free throws by that team.

ORR is a useful statistic because offensive rebounds can lead to second-chance scoring opportunities, which can be critical in close games. A team with a high ORR is generally considered to be more effective at controlling the boards and generating additional scoring opportunities.

ORR can be calculated for individual players as well as for teams. The formula for ORR is:

ORR = Offensive rebounds / (Offensive rebounds + Opponents' defensive rebounds)
   
  """)


####################################################################################################
st.write(
    """ ### Free Throw Rate (How often the given team shoots Free Throws)  [FTR] """)

st.write(""" Free Throw Rate (FTR) is a basketball statistic that measures how often a team attempts free throws in relation to their field goal attempts. It is calculated by dividing the number of free throw attempts by the number of field goal attempts.

The formula for Free Throw Rate is:

FTR = Free Throw Attempts / Field Goal Attempts

The resulting FTR value is a ratio, expressed as a decimal or a percentage. A higher FTR indicates that a team is more aggressive in attacking the basket and drawing fouls, which can be advantageous since free throws are uncontested shots that can lead to points without using the clock.
Free throw rate can be used to analyze a team's offensive strategy and the effectiveness of individual players in drawing fouls and getting to the free-throw line.
   
  """)


############################################################################################################
st.write(
    """ ### Two-Point Shooting Percentage """)

st.write(""" Free Throw Rate (FTR) is a basketball statistic that measures how often a team attempts free throws in relation to their field goal attempts. It is calculated by dividing the number of free throw attempts by the number of field goal attempts.

The formula for Free Throw Rate is:

FTR = Free Throw Attempts / Field Goal Attempts

The resulting FTR value is a ratio, expressed as a decimal or a percentage. A higher FTR indicates that a team is more aggressive in attacking the basket and drawing fouls, which can be advantageous since free throws are uncontested shots that can lead to points without using the clock.
Free throw rate can be used to analyze a team's offensive strategy and the effectiveness of individual players in drawing fouls and getting to the free-throw line.
   
  """)


######################################################################################################
st.write(
    """ ### Three-Point Shooting Percentage  """)

st.write(""" Free Throw Rate (FTR) is a basketball statistic that measures how often a team attempts free throws in relation to their field goal attempts. It is calculated by dividing the number of free throw attempts by the number of field goal attempts.

The formula for Free Throw Rate is:

FTR = Free Throw Attempts / Field Goal Attempts

The resulting FTR value is a ratio, expressed as a decimal or a percentage. A higher FTR indicates that a team is more aggressive in attacking the basket and drawing fouls, which can be advantageous since free throws are uncontested shots that can lead to points without using the clock.
Free throw rate can be used to analyze a team's offensive strategy and the effectiveness of individual players in drawing fouls and getting to the free-throw line.
   
  """)


###########################################################################################
st.write(
    """ ### Wins Above Bubble  """)

st.write(""" Free Throw Rate (FTR) is a basketball statistic that measures how often a team attempts free throws in relation to their field goal attempts. It is calculated by dividing the number of free throw attempts by the number of field goal attempts.

The formula for Free Throw Rate is:

FTR = Free Throw Attempts / Field Goal Attempts

The resulting FTR value is a ratio, expressed as a decimal or a percentage. A higher FTR indicates that a team is more aggressive in attacking the basket and drawing fouls, which can be advantageous since free throws are uncontested shots that can lead to points without using the clock.
Free throw rate can be used to analyze a team's offensive strategy and the effectiveness of individual players in drawing fouls and getting to the free-throw line.
   
  """)

st.write(""" ### Effective Field Goal Percentage Allowed  ##  """)

st.write(""" Effective Field Goal Percentage (eFG%) is a basketball statistic that measures a player's shooting efficiency. It is a modification of the traditional Field Goal Percentage (FG%), which only takes into account two-point field goals and three-point field goals.
In contrast, eFG% takes into account the fact that three-point field goals are worth more than two-point field goals. The formula for eFG% is:  

eFG% = (FGM + 0.5 * 3PM) / FGA  

where FGM is the number of field goals made, 3PM is the number of three-point field goals made, and FGA is the number of field goal attempts.  
By adding 0.5 times the number of three-pointers made to the number of two-pointers made in the numerator, eFG% effectively weights three-pointers as if they were 1.5 two-pointers. This provides a more accurate picture of a player's shooting efficiency and helps to compare players who shoot a different mix of two-pointers and three-pointers.  
eFG% is particularly useful for evaluating players who are efficient at shooting three-pointers. For example, a player who shoots 50% on two-point field goals and 33% on three-point field goals would have a FG% of 43.3%, which is below average. However, their eFG% would be 51.7%, which is above average because their three-pointers are weighted more heavily.   
   

  """)

st.write(""" ###  Turnover Percentage Allowed (Turnover Rate)  """)

st.write(""" Turnover Percentage Committed, also known as Steal Rate, is a basketball statistic that measures the percentage of possessions in which a player commits a steal. It is calculated as follows:

Steal Rate = (Steals x (Team Minutes / 5)) / Minutes Played

Where "Team Minutes" refers to the total number of minutes played by the player's team, and "Minutes Played" refers to the total number of minutes played by the player.
Steal Rate is used to evaluate a player's defensive ability and effectiveness in causing turnovers. A high Steal Rate indicates that a player is skilled at anticipating and disrupting passing lanes, and is successful at stealing the ball from opposing players.   
   
  """)
st.write(""" ### Free Throw Rate Allowed     ##  """)

st.write(""" Free Throw Rate (FTR) is a basketball statistic that measures how often a team attempts free throws in relation to their field goal attempts. It is calculated by dividing the number of free throw attempts by the number of field goal attempts.

The formula for Free Throw Rate is:

FTR = Free Throw Attempts / Field Goal Attempts

The resulting FTR value is a ratio, expressed as a decimal or a percentage. A higher FTR indicates that a team is more aggressive in attacking the basket and drawing fouls, which can be advantageous since free throws are uncontested shots that can lead to points without using the clock.
Free throw rate can be used to analyze a team's offensive strategy and the effectiveness of individual players in drawing fouls and getting to the free-throw line.
   
   

  """)
