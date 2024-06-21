import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load the saved model
model = pickle.load(open('finalized_model_G33.sav', 'rb'))

# Create input fields
st.markdown("<h1 style='text-align: center;'>Institute of Technology of Cambodia</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>Department of Applied Mathematic and Statistic </h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>Loan Eligibility Prediction 🏦</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Prediction and Deployment by Group 03 </h3>", unsafe_allow_html=True)

# Input fields
st.write('Enter applicant details:')
gender = st.selectbox('🚻 Gender', ['Male', 'Female'])  # 🚻 - restroom symbol
married = st.selectbox('👫 Married', ['Yes', 'No'])  # 👫 - couple holding hands
dependents = st.selectbox('👪 Dependents', ['0', '1', '2', '3+'])  # 👪 - family
education = st.selectbox('🎓 Education', ['Graduate', 'Not Graduate'])  # 🎓 - graduation cap
self_employed = st.selectbox('🧑‍💼 Self Employed', ['Yes', 'No'])  # 🧑‍💼 - office worker
Applicant_income = st.number_input('💵 Applicant income')  # 💵 - dollar banknote
Coapplicant_income = st.number_input('💶 Coapplicant income')  # 💶 - euro banknote
loan_amount = st.number_input('💸 Loan Amount')  # 💸 - money with wings
loan_amount_term = st.number_input('📅 Loan Amount Term')  # 📅 - calendar
credit_history = st.selectbox('💳 Credit History', ['1.0', '0.0'])  # 💳 - credit card
property_area = st.selectbox('🏡 Property Area', ['Urban', 'Semiurban', 'Rural'])  # 🏡 - house with garden



# Convert categorical variables
gender = 1 if gender == 'Female' else 0
married = 1 if married == 'Yes' else 0
education = 1 if education == 'Graduate' else 0
self_employed = 1 if self_employed == 'Yes' else 0
property_area = {'Urban': 0, 'Rural': 1, 'Semiurban': 2}[property_area]
dependents = {'0': 0, '1': 1, '2': 2, '3+': 3}[dependents]
credit_history = 1 if credit_history == '1.0' else 0

# Calculate
Applicant_income_log = np.log(Applicant_income) if Applicant_income > 0 else 0
Coapplicant_income_log = np.log(Coapplicant_income) if Coapplicant_income > 0 else 0
loan_amount_log = np.log(loan_amount) if loan_amount > 0 else 0
loan_amount_term_log = np.log(loan_amount_term) if loan_amount_term > 0 else 0

# Create a button to predict
if st.button('Predict'):
    # Create a dataframe from the inputs
    data = {
        'Gender': [gender],
        'Married': [married],
        'Dependents': [dependents],
        'Education': [education],
        'Self_Employed': [self_employed],
        'Applicant_Income': [Applicant_income_log],
        'Coapplicant_Income': [Coapplicant_income_log],
        'LoanAmount': [loan_amount_log],
        'Loan_Amount_Term': [loan_amount_term_log],
        'Credit_History': [credit_history],
        'Property_Area': [property_area],
    }
    df = pd.DataFrame(data)

    # Use the model to predict
    prediction = model.predict(df)

    # Display the prediction
    if prediction == 1:

        st.success('Congratulations! Your loan has been approved! 🎉😊')
    else:
        st.error('Unfortunately, your loan has not been approved. 😔❌')





