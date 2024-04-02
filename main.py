import streamlit as st
from streamlit_option_menu import option_menu

import about
import Anemia_Prediction
st.set_page_config(page_title="Anemia Prediction Web Application")
with st.sidebar:
    application = option_menu(
        menu_title='Anemia',
        options=['Anemia_Prediction', 'About'],
        icons=['trophy-fill','info-circle'],
        default_index=1,
        styles={
            "container": {"padding": "5!important", "background-color": "black",
                          "icon": {"color": "white", "font-size": "23px"},
                          "nav-link": {"color": "white", "font-size": "20px", "text-align": "left"},
                          "nav-link-selected": {"background-color": "#02ab21"},
                          }
        }
    )
if(application=='About'):
    about.app()
if(application=='Anemia_Prediction'):
    Anemia_Prediction.app()

##m=st.sidebar.selectbox("About or Predict",("about","Anemia_Prediction"))
#if(m=="Anemia_Prediction"):
 #   Anemia_Prediction.app()
#if(m=="about"):
   # about.app()


