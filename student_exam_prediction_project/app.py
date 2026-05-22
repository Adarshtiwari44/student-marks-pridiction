import streamlit as st
import numpy as np
import joblib

model = joblib.load("model.pkl")

st.set_page_config(page_title="Student Exam Score Predictor", layout="centered")

st.title("🎓 Student Exam Score Predictor")
st.write("Predict a student's exam score based on daily habits")

study_hours = st.slider("📘 Study hours per day", 0.0, 12.0, 2.0)
attendance = st.slider("🏫 Attendance Percentage", 0.0, 100.0, 80.0)
mental_health = st.slider("🧠 Mental Health Rating (1–10)", 1, 10, 5)
sleep_hours = st.slider("😴 Sleep Hours per Night", 0.0, 12.0, 6.0)
part_time_job = st.selectbox("💼 Part-time Job", ["No", "Yes"])

ptj_encoded = 1 if part_time_job == "Yes" else 0

if st.button("📊 Predict Exam Score"):
    input_data = np.array([[study_hours, attendance, ptj_encoded, sleep_hours, mental_health]])
    prediction = model.predict(input_data)[0]
    prediction = max(0, min(100, prediction))
    st.success(f"✅ Predicted Exam Score: {prediction:.2f} / 100")
