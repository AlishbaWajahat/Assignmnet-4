import streamlit as st

height=st.slider("Select your height in (cm)",max_value=250,min_value=100)
weight=st.slider("Select your weight in (kg)",max_value=150,min_value=40)

if st.button("Calculate"):
    bmi=weight/((height/100)**2)
    st.write(f"Your BMI value is {bmi}")


st.write("### BMI Categories ###")
st.write("- Underweight: BMI less than 18.5")
st.write("- Normal weight: BMI between 18.5 and 24.9")
st.write("- Over weight: BMI between 25 and 29.9")
st.write("- Obesity: BMI 30 orgreater than 30")
