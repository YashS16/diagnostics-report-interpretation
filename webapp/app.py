import streamlit as st
from keras.models import load_model
from PIL import Image
import numpy as np
from streamlit_option_menu import option_menu

from util import classify, set_background


st.set_page_config(
    page_title="Diagnosis at Home",
    page_icon="👨‍⚕️",
)

st.write("# Welcome to Diagnostics Report Analysis! 👋")
#set_background('./bgs/.jpg')

# sidebar for navigation, idk how to connect side bar to the pages
#with st.sidebar:

    #selected = option_menu('Diseases Prediction System',

                          #['COVID19 Prediction',
                           #'Brain Tumor Prediction'],
                          #icons=['mask','heart'],
                          #menu_icon="cast",
                          #default_index=0,
                          #orientation="horizontal")
st.markdown(
    """
    Diagnostics Report Analysis is an free app that we created in the hope of
    making the diagnostic process more easily available and maybe ease the pressure on the doctors all around the world!

    **👈 Select a diagnostic method from the sidebar** and get an accurate prediction for either COVID19 or Brain tumor.
    ### What's our goal 🎯?
    - Reduce waiting time for patientes and less stress for doctors.
    - Limiting the spread of illness like COVID

    ### Sources:
    - Dataset for COVID19 [Covid19 detection using Tensorflow from Chest Xray](https://www.kaggle.com/code/ankan1998/covid19-detection-using-tensorflow-from-chest-xray/notebook)
    - Dataset for Brain tumor's [MRI](https://www.kaggle.com/datasets/sartajbhuvaji/brain-tumor-classification-mri)
"""
)
