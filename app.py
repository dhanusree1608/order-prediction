import streamlit as st
import joblib
import pandas as pd

model = joblib.load('order_model.joblib')

st.title('Will the customer order this product?')

review = st.slider('Review rating', 1.0, 5.0, 4.0, 0.5)
quality = st.slider('Quality rating', 1, 5, 4)
price = st.number_input('Price (₹)', min_value=100, max_value=2000, value=500, step=10)

if st.button('Predict'):
    row = pd.DataFrame([[review, quality, price]],
                       columns=['Review rating', 'Quality rating', 'Price (₹)'])
    prob = model.predict_proba(row)[0, 1]
    if prob >= 0.5:
        st.success(f'ORDERED (chance of ordering: {prob:.0%})')
    else:
        st.error(f'NOT ORDERED (chance of ordering: {prob:.0%})')
