#import modules
import pandas as pd
import joblib
import streamlit as st

#load model and encoder
model = joblib.load('antibiotic_model.pkl')
encoder = joblib.load('antibiotic_encoder.pkl')

#sidebar
name = "AIToolForge Technology"
goal = "To detects weather patient is resistant to antibiotics or not."
st.sidebar.title("ABOUT US!")
st.sidebar.caption(f"Developer: {name}.")
st.sidebar.title("CONTACT CEO...")
st.sidebar.link_button("Facebook","https://www.facebook.com/sadeeq.ahjinuwa")
st.sidebar.link_button("email",'mailto:sadiqinuwa6@gmail.com')
st.sidebar.link_button("WhatsApp",'https://wa.me/2347067717477')
st.title("ANTIBIOTICS RESISTANCE")
st.caption(f"GOAL: {goal}")
#converting to streamlit
Organism = st.selectbox("Select The Detected Organism", ["E_coli","Klebsiella","Pseudomonas","S_aureus"])
Gram_Stain = st.selectbox("Select The Gram-Staining", ["Negative","Positive"])
ESBL = st.selectbox("Select If the Evaluated ESBL, Yes Or No", ["Yes","No"])
MIC = st.number_input("Enter The Evaluated MIC value")
Patient_Age = st.number_input("Enter The Patient_Age value")
Previous_Antibiotic_Exposure = st.selectbox("Select Previous_Antibiotic_Exposure(Yes/No)", ["Yes","No"])
Hospital_Ward = st.selectbox("Select The Hospital_Ward", ["Surgical","Medical","ICU","Outpatient"])

if st.button("Make Detection"):
    real_data = pd.DataFrame({
        "Organism": [Organism],
        "Gram_Stain": [Gram_Stain],
        "ESBL": [ESBL],
        "MIC": [MIC],
        "Patient_Age": [Patient_Age],
        "Previous_Antibiotic_Exposure": [Previous_Antibiotic_Exposure],
        "Hospital_Ward": [Hospital_Ward]
    })



    predicted_data = encoder.transform(real_data)

    prediction = model.predict(predicted_data)
    st.success("Resistant" if prediction == 1 else "Non-resistant")


