# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

# Theme
theme_plotly = None  # None or streamlit

# Layout
st.set_page_config(page_title=' Most Effective Factors - Who Will Win 2023 March Madness',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('🔥 Key Variables')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache_data()
def get_data(query):
    if query == 'Barttorvik_Team':
        return pd.read_csv('Data/barttorvik_2023.csv')
    elif query == 'sensetive_analyse':
        return pd.read_csv('Data/weights_O.csv')
    return None


Barttorvik_Team = get_data('Barttorvik_Team')
sensetive_analyse = get_data('sensetive_analyse')


df = Barttorvik_Team
df2 = sensetive_analyse

#################################################################################################
st.write(""" ### Sensivity Analysis of Key Variables ##  """)

st.write("""
 Sensitivity analysis is a crucial tool for understanding the impact of various factors on March Madness winner prediction. In this dashboard, the key variables are determined through a sensitivity analysis that involves varying the value of the variable and observing its effect on the prediction outcome. This process helps to identify which factors have the most significant impact on the prediction accuracy, enabling us to refine our models and improve our ability to predict the winner of the tournament. By conducting sensitivity analysis we tried to gain better insights into the complex relationships between different variables and optimized our predictions for the most accurate results.

  """)

st.info(""" ##### The  List of Variables and Features on this project : ####   """)

c1, c2 = st.columns(2)

with c1:

    st.info("""

1. Win Rate
2. BARTHAG   
3. Turnover Percentage Committed (Steal Rate)
4. Offensive Rebound Rate  
5. Free Throw Rate (How often the given team shoots Free Throws)  
6. Two-Point Shooting Percentage   
7. Three-Point Shooting Percentage    
8. Wins Above Bubble
9. Adjusted Offensive Efficiency

        """)
with c2:
    st.info(""" 

10. Effective Field Goal Percentage Shot    
11. ADJDE: Adjusted Defensive Efficiency 
12. ADJ_T: Adjusted Tempo       
13. EFG_D: Effective Field Goal Percentage Allowed  
14. TOR: Turnover Percentage Allowed (Turnover Rate)  
15. DRB: Offensive Rebound Rate Allowed   
16. FTRD: Free Throw Rate Allowed   
17. 2P_D: Two-Point Shooting Percentage Allowed      
18. 3P_D: Three-Point Shooting Percentage Allowed  
        """)

###################################################################


st.write(""" ##  Definition and Calculation Formula ##  """)

st.write(""" There are a total of 18 variables and statistics for each team in this dashboard that were taken from Battrovik and Kenpom. The Glossary section at the bottom of this dashboard has a list of these variables' comprehensive definitions and formulas. The only parameter we tweaked was win rate, and it wasn't in the site tables, which is Simply divide the total number of games one team played over the entire season by the number of victories. and the Barthag is a prediction of a team's likelihood of triumphing over the typical DI team. Since it ranges from 0 to 1, higher is preferable. The exponent, a constant, is utilized in the Barthag calculation. It is common in NCAA rankings to evaluate teams based on their Barthag. 
""")
#####################################################


st.write(""" ### Sensivity Analysis of Key Variables and Features ##  """)

st.write("""
In this case, the model has 18 inputs, and the goal is to find the six most effective ones. The first step in sensitivity analysis is to vary each input while holding all other inputs constant and observe the effect on the output. This process is repeated for all 18 inputs, and the resulting data is analyzed to determine which inputs have the most significant impact on the output.
One common method for analyzing the data is to use a sensitivity index, such as the Morris method or the Sobol' method. These methods provide a quantitative measure of the sensitivity of each input.   
Once the sensitivity indices were calculated, the six inputs with the highest indices were identified as the most effective inputs, which are "win rate," "offensive rebound rate allowed," "adjusted offensive efficiency," "Barthag," "turnover percentage committed (steal rate)," and "adjusted defensive efficiency." . These inputs have the greatest influence on the output of the model and are therefore the most important to consider when making decisions based on the model's results.
It is important to note that sensitivity analysis is not a one-time process. As the model or its inputs change, the sensitivity analysis must be repeated to ensure that the most effective inputs are still accurate.

 """)


st.write(""" 

  """)

fig = px.bar(df2, x="parameters", y="sensitivity",
             title='Parameters Sensivity analysis', log_y=False)
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Sensitivity')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
