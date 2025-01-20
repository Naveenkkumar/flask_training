import pandas as pd
import streamlit as st
import requests

st.title('Titanic passengers survival prediction')

st.write('This is a simple example of a Machine Learning model deployment using Streamlit.')


user_input_pclass = st.selectbox('Pclass', [1, 2, 3])
user_input_sex = st.selectbox('Sex', ['Male', 'Female'])
user_input_age = st.number_input('Age', min_value=0, max_value=100, value=30)


if st.button('Predict'):
    #send input data to Flask API
    response = requests.post('http://localhost:8501/predict', json={'Pclass': user_input_pclass, 'Sex': user_input_sex, 'Age': user_input_age})
                                                                    
    if response.status_code == 200:
        st.write('Prediction:', response.text)
    else:
        st.write('Error:', response.text)
        

else:
    st.write('Please input values to predict survival')