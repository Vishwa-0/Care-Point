import streamlit as st
import joblib
import os
import numpy as np

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Care Point",
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
st.markdown("<p class='subtle'>A minimal diabetes risk signal tool</p>", unsafe_allow_html=True)

st.markdown("---")

# ---------------- Layout ----------------
left, center, right = st.columns([1.2, 1.6, 1.2])

# ---------------- Inputs ----------------
with left:
    st.markdown("### Patient Inputs")
    st.markdown("Numeric indicators only. No data is stored.")

    st.markdown("---")

    age = st.slider("Age (years)", 1, 120, 35)
    mass = st.number_input("Body Mass (kg)", min_value=30.0, max_value=200.0, step=0.5)
    insu = st.number_input("Insulin Level", min_value=2.0, step=0.1)
    plas = st.number_input("Plasma Glucose", min_value=25.0, step=0.1)

    family_history = st.radio(
        "Family History of Diabetes",
        ["No", "Yes"],
        horizontal=True
    )

    calculate = st.button("Assess Risk", use_container_width=True)

# ---------------- Context ----------------
with center:
    st.markdown("### Context & Assumptions")
    st.markdown("This tool provides a **statistical risk estimate**, not a diagnosis.")

    st.markdown("---")

    st.markdown("""
    **Model notes:**
    - Trained on historical patient data
    - Uses linear decision boundaries
    - Best interpreted as a screening signal
    """)

    st.info("Consult a qualified healthcare professional for medical advice.")

# ---------------- Output ----------------
with right:
    st.markdown("### Risk Output")
    st.markdown("Model-generated diabetes risk category.")

    st.markdown("---")

    if calculate:
        family_val = 1 if family_history == "Yes" else 0
        features = np.array([[age, mass, insu, plas]])
        prediction = model.predict(features)[0]
        if risk_prob < 0.3:
            st.success(f"Low risk ({risk_prob:.2%})")
        elif risk_prob < 0.6:
            st.warning(f"Moderate risk ({risk_prob:.2%})")
        else:
            st.error(f"High risk ({risk_prob:.2%})")

    else:
        st.info("Enter values and assess risk")
        st.progress(10)

# ---------------- Footer ----------------
st.markdown("---")
st.caption("Care Point • Decision support, not medical advice")
