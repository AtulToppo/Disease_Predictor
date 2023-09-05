import pickle
import streamlit as st
import pandas as pd

#loading the saved models
diabetes_model = pickle.load(open(r'C:\Users\atul toppo\Documents\Disease Predictor\models\diabetes_modal.pkl','rb'))
heart_model = pickle.load(open(r'C:\Users\atul toppo\Documents\Disease Predictor\models\heart_modal.pkl','rb'))
breast_model =pickle.load(open(r'C:\Users\atul toppo\Documents\Disease Predictor\models\breast_modal.pkl','rb'))

#sidebar for navigate

with st.sidebar:
    st.markdown("<h1 style='text-align: center;'>Multiple Disease Prediction</h1>", unsafe_allow_html=True)
    selected = st.selectbox(' ',['Diabetes','Heart','Breast-Cancer'])

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
        BloodPressure = st.text_input("Blood Pressure Level(mm Hg):")
    with col1:
        SkinThickness = st.text_input("SkinThickness(mm):")
    with col2:
        Insulin = st.text_input("Insulin level(mu U/ml):")
    with col3:
        BMI = st.text_input("BodyMassIndex(weight in kg/(height in m)^2):")
    with col1:
        DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction value:")
    with col2:
        Age = st.text_input("Age of Person(years):")
    
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
if(selected == 'Heart'):
    #page Title
    st.title("Heart Disease Prediction using ml")

    #getting input data
    col1,col2,col3 = st.columns(3)
    with col1:
        Age = st.text_input("Age of the Person(years):")
    with col2:
        Sex = st.text_input("Gender(M=1,F=0):")
    with col3:
        ChestPainType = st.selectbox('Chest Pain Type:',['Atypical Angina',
                                              'Non-Anginal Pain','Asymptomatic','Typical Angina'])
    with col1:
        RestingBP = st.text_input("RestingBP(mm Hg):")
    with col2:
        Cholesterol = st.text_input("Cholesterol level(mg/dl):")
    with col3:
        FastingBS = st.selectbox('Fasting Blood Sugar(> 120 mg/dl):',['True','False'])
    with col1:
        RestingECG = st.selectbox('Resting  Electrocardiographic Results:',['Normal','ST-T wave Abnormality','left ventricular hypertrophy'])
    with col2:
        MaxHR = st.text_input("MaxHR:")
    with col3:
        ExerciseAngina = st.selectbox('Exercise Induced Angina:',['Yes','No'])
    with col1:
        Oldpeak = st.text_input("Oldpeak:")
    with col2:
        ST_Slope = st.selectbox('ST_Slope',['UpSloping','Flat','DownSloping'])

    #assigning values
    if(ChestPainType == 'Atypical Angina'):
        ChestPainType=0
    elif(ChestPainType == 'Non-Anginal Pain'):
        ChestPainType=1
    elif(ChestPainType == 'Asymptomatic'):
        ChestPainType=2
    elif(ChestPainType == 'Typical Angina'):
        ChestPainType=3

    if(FastingBS == 'True'):
        FastingBS=1
    elif(FastingBS == 'False'):
        FastingBS=0

    if(RestingECG == 'Normal'):
        RestingECG=0
    elif(RestingECG == 'ST-T wave Abnormality'):
        RestingECG=1
    elif(RestingECG == 'left ventricular hypertrophy'):
        RestingECG=2

    if(ExerciseAngina == 'Yes'):
        ExerciseAngina=1
    elif(ExerciseAngina == 'No'):
        ExerciseAngina=0

    if(ST_Slope == 'UpSloping'):
        ST_Slope=0
    elif(ST_Slope == 'Flat'):
        ST_Slope=1
    elif(ST_Slope == 'DownSloping'):
        ST_Slope=2

    #code for diagnosis
    heart_diagnosis = ''
    #creating a button for prediction
    if st.button('Heart Disease Test Result:'):
        heart_prediction = heart_model.predict([[Age,Sex,ChestPainType,RestingBP,Cholesterol,FastingBS,RestingECG,MaxHR,ExerciseAngina,Oldpeak,ST_Slope]])
        if(heart_prediction[0] == 1):
            heart_diagnosis=" The person has heart disease"
        else:
            heart_diagnosis="The person does not have heart disease"
    st.success(heart_diagnosis)
if(selected == 'Breast-Cancer'):
    #page Title
    st.title("Breast-Cancer Prediction using ml")

     #getting input data
    col1,col2,col3 = st.columns(3)
    with col1:
        radius_mean = st.text_input("Mean_Radius of Lobes(cm):")
    with col2:
        texture_mean = st.text_input("Mean of Surface Texture(cm):")
    with col3:
        perimeter_mean = st.text_input("Outer Perimeter of Lobes(cm):")
    with col1:
        area_mean = st.text_input("Mean Area of Lobes(cm^2):")
    with col2:
        smoothness_mean = st.text_input("Mean of Smoothness Levels(cm):")
    with col3:
        compactness_mean = st.text_input("Mean of Compactness(cm):")
    with col1:
        concavity_mean = st.text_input("Mean of Concavity(cm):")
    with col2:
        concave_points_mean = st.text_input("Mean of Cocave Points(cm):")
    with col3:
        symmetry_mean = st.text_input("Mean of Symmetry(cm):")
    with col1:
        fractal_dimension_mean = st.text_input("Mean of Fractal Dimension(cm):")
    with col2:
        radius_se = st.text_input("SE of Radius(cm):")
    with col3:
        texture_se = st.text_input("SE of Texture(cm):")
    with col1:
        perimeter_se = st.text_input("Perimeter of SE(cm):")
    with col2:
        area_se = st.text_input("Area of SE(cm^2):")
    with col3:
        smoothness_se = st.text_input("SE of Smoothness(cm):")
    with col1:
        compactness_se = st.text_input("SE of compactness(cm):")
    with col2:
        concavity_se = st.text_input("SEE of concavity(cm):")
    with col3:
        concave_points_se = st.text_input("SE of concave points(cm):")
    with col1:
        symmetry_se = st.text_input("SE of symmetry(cm):")
    with col2:
        fractal_dimension_se = st.text_input("SE of Fractal Dimension(cm):")
    with col3:
        radius_worst = st.text_input("Worst Radius(cm):")
    with col1:
        texture_worst = st.text_input("Worst Texture(cm):")
    with col2:
        perimeter_worst = st.text_input("Worst Permimeter(cm):")
    with col3:
        area_worst = st.text_input("Worst Area(cm^2):")
    with col1:
        smoothness_worst = st.text_input("smoothness_worst(cm):")
    with col2:
        compactness_worst = st.text_input("Worse Compactness(cm):")
    with col3:
        concavity_worst = st.text_input("Worst Concavity:")
    with col1:
        concave_points_worst = st.text_input("Worst Concave Points(cm):")
    with col2:
        symmetry_worst = st.text_input("Worst Symmetry:")
    with col3:
        fractal_dimension_worst = st.text_input("Worst Fractal Dimension:")
    
    #code for diagnosis
    breast_diagnosis = ''
    #creating a button for prediction
    if st.button('Breast Cancer Test Result:'):
        Breast_prediction = breast_model.predict([[radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,concave_points_mean,
        symmetry_mean,fractal_dimension_mean,radius_se,texture_se,perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,
        concave_points_se,symmetry_se,fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,
        compactness_worst,concavity_worst,concave_points_worst,symmetry_worst,fractal_dimension_worst]])
        if(Breast_prediction[0] == 1):
            breast_diagnosis=" The person has Breast Cancer"
        else:
            breast_diagnosis="The person does not have Breast Cancer"
    st.success(breast_diagnosis)



