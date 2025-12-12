import streamlit as st
import joblib
import os

st.title("Care Point")

st.header("Purpose")
st.write("This tool provides a basic diabetes risk estimation based on user-entered information.")

st.header("Disclaimer")
st.write("NOTE: This tool does not provide medical advice, diagnosis, or treatment. Consult a healthcare professional for medical concerns.")

st.subheader("You will be asked for:")
st.write("- Age")
st.write("- Mass")
st.write("- Insulin")
st.write("- Plasma")
st.write("- Family History (yes/no)")

st.write("The tool uses your inputs to generate a simple risk categorization for diabetes. No data is stored.")

st.write("---")
st.header("Enter Your Information")

age = st.number_input("Age", min_value=1, max_value=120, step=1)
mass = st.number_input("Mass (kg)", min_value=1.0, step=0.1)
insu = st.number_input("Insulin", min_value=2.0, step=0.1)
plas = st.number_input("Plasma", min_value=25.0, step=0.1)
family_history = st.selectbox("Family History of Diabetes?", ["No", "Yes"])

st.write("---")
st.header("Risk Assessment")

MODEL_PATH = os.path.join(os.path.dirname(__file__), "diabetes.pkl")
model = joblib.load(MODEL_PATH)

pred = model.predict([[age, mass, insu, plas]])

st.write("Predicted risk:", pred[0])
