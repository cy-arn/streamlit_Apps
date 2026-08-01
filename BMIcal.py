import google.genai as genai
import streamlit as st
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]

client = genai.Client(api_key=GOOGLE_API_KEY)

st.title("BMI calculator with AI")

# 1. Get user input
weight = st.number_input("Enter weight in kg: ")
height = st.number_input("Enter height in meters: ")

# 2. Calculate BMI
bmi = weight / (height**2)
st.write(f"Your BMI is: {bmi:.2f}")
prompt = f"My BMI is {bmi:.2f}. Tell me what this means simply and kindly in four line."

if st.button('Analyze your BMI with AI:'):
    st.write("Analyzing your BMI with AI...")
    response = client.models.generate_content(
     model="gemini-3.6-flash",
     contents=prompt
    )
    st.write(response.text)
