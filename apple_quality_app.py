import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image

# Load the modelpip install -r requirements.txt
model = pickle.load(open('model/Kneighbors.sav', 'rb'))

# Define the Streamlit app
st.title('Apple Quality Prediction') 
st.image("https://www.bangaloreagrico.in/wp-content/uploads/2018/01/apple-plant-bangalore-agrico.jpg", width=200)
st.write("This prediction application aims to predict the quality of apples based on certain measurements included in the dataset")
st.title("Dataset Source :")
st.markdown("<https://www.kaggle.com/datasets/nelgiriyewithana/apple-quality>") 
st.title("Please input prediction variables :")
feature_list = dict()

# Add input widgets for user input
feature_list['Size'] = st.text_input('Enter Size:')
feature_list['Weight'] = st.text_input('Enter Weight:')
feature_list['Sweetness'] = st.text_input('Enter Sweetness:')
feature_list['Crunchiness'] = st.text_input('Enter Crunchiness')
feature_list['Juiciness'] = st.text_input('Enter Juiciness:')
feature_list['Ripeness'] = st.text_input('Enter Ripeness:')
feature_list['Acidity'] = st.text_input('Acidity:')

# Add a button to make predictions
if st.button('Predict'):
    # Perform predictions
    df_feature_list = pd.DataFrame(data=np.array(list(feature_list.values())).reshape(1,-1), columns=feature_list.keys())
    df_feature_list = df_feature_list.astype(float)

    prediction = model.predict(df_feature_list)
    output = prediction[0]
    if output == 'good':
        st.success('Prediction: good')
    else:
        st.error('Prediction: bad')
