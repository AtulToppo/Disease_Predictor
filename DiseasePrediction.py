import pickle
import streamlit as st
from streamlit_option_menu import option_menu

primaryColor="#F63366"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"

#loading the saved models
diabetes_model = pickle.load(open(r'C:\Users\atul toppo\Documents\Disease Predictor\models\diabetes_modal.pkl','rb'))

#sidebar for navigate

with st.sidebar:
    selected = option_menu('Multiple Disease prediction',['Diabetes'],
                                        icons=["person"],
                                        default_index=0)

#Diabetes prediction page
if(selected == 'Diabetes'):
    #page Title
    st.title("Diabetes Prediction using ml")

    #getting input data
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input("No. of Pregnancies:")
    with col2:
        Glucose = st.text_input("Glucose Level:")
    with col3:
        BloodPressure = st.text_input("Blood Pressure Level:")
    with col1:
        SkinThickness = st.text_input("SkinThickness:")
    with col2:
        Insulin = st.text_input("Insulin level:")
    with col3:
        BMI = st.text_input("BodyMassIndex:")
    with col1:
        DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction value:")
    with col2:
        Age = st.text_input("Age of Person:")
    
    #code for diagnosis
    diab_diagnosis = ''
    #creating a button for prediction
    if st.button('Diabetes Test Result:'):
        diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI
        ,DiabetesPedigreeFunction,Age]])
        if(diab_prediction[0] == 1):
            diab_diagnosis=" The person is Diabetic"
        else:
            diab_diagnosis="The person is not Diabetic"
    st.success(diab_diagnosis)

