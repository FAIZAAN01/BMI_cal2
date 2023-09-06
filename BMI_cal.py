import streamlit as st

# Define the title and header of the web app
st.title("BMI Calculator")
st.header("Calculate your Body Mass Index (BMI)")

# Create input fields for height and weight
height = st.number_input("Enter your height (in meters)", min_value=0.01, max_value=3.0, step=0.01)
weight = st.number_input("Enter your weight (in kilograms)", min_value=1.0, max_value=500.0, step=0.1)

# Calculate BMI
if st.button("Calculate BMI"):
    bmi = weight / (height ** 2)
    st.write(f"Your BMI is: {bmi:.2f}")

    # Interpret the BMI value
    if bmi < 18.5:
        st.warning("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.success("You have a normal weight.")
    elif 24.9 <= bmi < 29.9:
        st.warning("You are overweight.")
    else:
        st.error("You are obese.")
