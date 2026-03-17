import streamlit as st

st.title("🏋️ BMI Calculator")


st.write("### Enter your height:")
feet = st.slider("Feet", 3, 8, 5)
inches = st.slider("Inches", 0, 11, 9)


weight = st.slider("Enter your weight (kg)", 40, 200, 70)


height_m = (feet * 12 + inches) * 0.0254


bmi = weight / (height_m ** 2)
st.write(f"### Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
elif 25 <= bmi < 29.9:
    category = "Pre-Obesity (Overweight)"
elif 30 <= bmi < 34.9:
    category = "Obesity Class I"
elif 35 <= bmi < 39.9:
    category = "Obesity Class II"
else:
    category = "Obesity Class III"

colors = {
    "Underweight": "blue",
    "Normal weight": "green",
    "Pre-Obesity (Overweight)": "orange",
    "Obesity Class I": "red",
    "Obesity Class II": "darkred",
    "Obesity Class III": "purple"
}

st.markdown(f"<h2 style='color:{colors[category]}'>{category}</h2>", unsafe_allow_html=True)

st.write("### BMI Categories (WHO / modern standards):")
st.write("• Underweight: BMI < 18.5")
st.write("• Normal weight: 18.5 ≤ BMI < 24.9")
st.write("• Pre-Obesity (Overweight): 25 ≤ BMI < 29.9")
st.write("• Obesity Class I: 30 ≤ BMI < 34.9")
st.write("• Obesity Class II: 35 ≤ BMI < 39.9")
st.write("• Obesity Class III: BMI ≥ 40")