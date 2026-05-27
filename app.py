import streamlit as st
import joblib
import pandas as pd

# 1. Load the saved model
model = joblib.load('test_score_model.pkl')

st.title("📚 Test Score Predictor")
st.write("Enter the number of hours studied to get a predicted test score.")

# 2. Create Input Field
hours = st.number_input("Hours Studied", min_value=0.0, max_value=24.0, value=6.0, step=0.5)

# 3. Predict Button
if st.button("Predict Score"):
    input_data = pd.DataFrame([[hours]], columns=['Hours_Studied'])

    prediction = model.predict(input_data)[0]

    st.success(f"### Predicted Test Score: {prediction:.2f} / 100")
