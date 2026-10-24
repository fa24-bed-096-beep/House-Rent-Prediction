import streamlit as st
import joblib
import numpy as np

# Saved model load karein
model = joblib.load('house_model.pkl')

st.title("House Price Prediction App")
st.write("Machine Learning Assignment 3 (AIC354)")

# User se input lene ke liye fields (Aap apnay dataset ke mutabiq features adjust kar sakte hain)
area = st.number_input("Enter House Area (e.g., sq ft):", min_value=0.0)
rooms = st.number_input("Enter Number of Rooms:", min_value=0.0)

if st.button("Predict Price"):
    # Input ko model ke format mein convert karna
    features = np.array([[area, rooms]])
    prediction = model.predict(features)
    st.success(f"Predicted House Price: ${prediction[0]:,.2f}")