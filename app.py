import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Page config
st.set_page_config(page_title="Calories Predictor", page_icon="🔥", layout="centered")

# Background image + styling
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("https://img.freepik.com/free-photo/alarm-clock-towel-dumbbells_23-2147735034.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    .main-box {{
        background: rgba(0, 0, 0, 0.7);
        padding: 25px;
        border-radius: 15px;
        color: white;
        position: relative;   /* IMPORTANT */
    }}

    h1 {{
        text-align: center;
        color: #ff4b4b;
        font-size: 40px;
    }}

    .stButton>button {{
        background: linear-gradient(90deg, #ff4b4b, #ff914d);
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 18px;
        border: none;
    }}

    /* Your name styling */
    .sticky-name {{
        position: absolute;
        bottom: 20px;
        right: 30px;
        font-size: 18px;
        font-weight: bold;
        font-style: italic;
        color: black;
    }}
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1>🔥 Calories Burnt Predictor</h1>", unsafe_allow_html=True)

# Main box
st.markdown('<div class="main-box">', unsafe_allow_html=True)

st.write("### Enter your fitness details 👇")

# Layout
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.slider("Age", 10, 80)
    height = st.number_input("Height (cm)", 100, 220)

with col2:
    weight = st.number_input("Weight (kg)", 30, 150)
    duration = st.slider("Workout Duration (min)", 1, 120)
    heart_rate = st.slider("Heart Rate", 60, 200)

body_temp = st.slider("Body Temperature (°C)", 35.0, 42.0)

# Convert gender
gender = 1 if gender == "Female" else 0

# Prediction
if st.button("🔥 Predict Calories"):
    input_data = np.array([[gender, age, height, weight, duration, heart_rate, body_temp]])
    prediction = model.predict(input_data)

    st.success(f"🔥 Calories Burned: {prediction[0]:.2f} kcal")

# 👇 YOUR NAME (BOTTOM RIGHT)
st.markdown(
    "<div class='sticky-name'>By - Shivangi Tripathi</div>",
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("<p style='text-align:center;color:white;'>Built with ❤️ using Machine Learning</p>", unsafe_allow_html=True)