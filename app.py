import streamlit as st
import joblib
import os
import numpy as np

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Care Point",
    page_icon="🩺",
    layout="wide"
)

# ---------------- Load Model ----------------
@st.cache_resource
def load_model():
    model_path = os.path.join(os.path.dirname(__file__), "diabetes.pkl")
    return joblib.load(model_path)

model = load_model()

# ---------------- Header ----------------
st.markdown("""
<style>
.big-title { font-size: 3rem; font-weight: 700; }
.subtle { color: #6c757d; }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='big-title'>Care Point</div>", unsafe_allow_html=True)
st.markdown("<p class='subtle'>Diabetes risk signals, not diagnoses</p>", unsafe_allow_html=True)

st.markdown("---")

# ---------------- Layout ----------------
left, center, right = st.columns([1.2, 1.6, 1.2])

# ---------------- Inputs ----------------
with left:
    st.markdown("### Patient Inputs")
    st.markdown("Numeric indicators only. No data is stored.")
    st.markdown("---")

    age = st.slider("Age (years)", 1, 120, 35)
    mass = st.number_input("Body Mass (kg)", min_value=30.0, max_value=200.0, step=0.5, value=70.0)
    insu = st.number_input("Insulin Level", min_value=2.0, step=0.1, value=80.0)
    plas = st.number_input("Plasma Glucose", min_value=25.0, step=0.1, value=120.0)

    calculate = st.button("Assess Risk", use_container_width=True)

# ---------------- Context ----------------
with center:
    st.markdown("### How to Read This")
    st.markdown("This tool estimates **relative diabetes risk** using a trained ML model.")
    st.markdown("---")

    st.markdown("""
    **Important notes:**
    - This is **not a diagnosis**
    - Risk is expressed as a probability
    - Lower risk does not mean no risk
    - Use this as a screening signal only
    """)

    st.info("Always consult a qualified healthcare professional for medical decisions.")

# ---------------- Output ----------------
with right:
    st.markdown("### Risk Output")
    st.markdown("Probability-based diabetes risk estimate.")
    st.markdown("---")

    if calculate:
        features = np.array([[age, mass, insu, plas]])
        
        risk_prob = model.predict_proba(features)[0][1]

        st.metric("Estimated Diabetes Risk", f"{risk_prob:.1%}")

        if risk_prob < 0.30:
            st.success("Low risk profile")
            st.progress(30)
        elif risk_prob < 0.60:
            st.warning("Moderate risk profile")
            st.progress(60)
        else:
            st.error("High risk profile")
            st.progress(85)

    else:
        st.info("Enter values and assess risk")
        st.progress(10)

# ---------------- Footer ----------------
st.markdown("---")
st.caption("Care Point • Decision support, not medical advice")
