import pandas as pd
import streamlit as st

st.title("BMI Calculator")

height = st.slider("Enter your height (cm):", 100, 250, 175)
weight = st.slider("Enter your weight (kg):", 40, 200, 75)

bmi = weight / ((height / 100) ** 2)

st.write(f"### Your BMI is {bmi:.2f}")

if bmi < 18.5:
    st.info("Category: Underweight")
elif 18.5 <= bmi < 25:
    st.success("Category: Normal weight")
elif 25 <= bmi < 30:
    st.warning("Category: Overweight")
else:
    st.error("Category: Obesity")