import streamlit as st

st.title("Care Point")

st.header("Purpose")
st.write("This tool provides a basic diabetes risk estimation based on user-entered information.")

st.header("Disclaimer")
st.write("NOTE: This tool does not provide medical advice, diagnosis, or treatment. Consult a healthcare professional for medical concerns.")

st.subheader("You will be asked for:")
st.write("- Age")
st.write("- Weight and Height (for BMI)")
st.write("- Fasting Glucose Level")
st.write("- Family History (yes/no)")
st.write("- Symptoms such as excessive thirst or frequent urination (yes/no)")

st.write("The tool uses your inputs to generate a simple risk categorization for diabetes. No data is stored.")

st.write("---")
st.header("Enter Your Information")

age = st.number_input("Age", min_value=1, max_value=120, step=1)
weight = st.number_input("Weight (kg)", min_value=1.0, step=0.1)
height = st.number_input("Height (cm)", min_value=30.0, step=0.1)
glucose = st.number_input("Fasting Glucose Level (mg/dL)", min_value=1.0, step=0.1)
family_history = st.selectbox("Family History of Diabetes?", ["No", "Yes"])
symptoms = st.selectbox("Symptoms (excessive thirst or frequent urination)?", ["No", "Yes"])

st.write("---")
st.header("Risk Assessment")

if st.button("Calculate Risk"):
    bmi = weight / ((height / 100) ** 2)

    risk_score = 0

    if age > 45:
        risk_score += 1
    if bmi > 25:
        risk_score += 1
    if glucose >= 126:
        risk_score += 2
    elif glucose >= 100:
        risk_score += 1
    if family_history == "Yes":
        risk_score += 1
    if symptoms == "Yes":
        risk_score += 1

    if risk_score <= 1:
        st.write("Risk Level: Low")
    elif risk_score <= 3:
        st.write("Risk Level: Moderate")
    else:
        st.write("Risk Level: High")

