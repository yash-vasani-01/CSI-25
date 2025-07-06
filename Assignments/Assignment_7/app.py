import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load trained pipeline
pipe = pickle.load(open('pipe.pkl', 'rb'))

# Title
st.title("Laptop Price Predictor 💻")

# Input Fields
company = st.selectbox("Brand", ['Toshiba', 'MSI', 'Asus', 'Dell', 'HP', 'Apple', 'Acer', 'Lenovo', 'Chuwi'])
typename = st.selectbox("Type", ['Notebook', 'Gaming', 'Netbook', '2 in 1 Convertible', 'Ultrabook', 'Workstation'])
ram = st.selectbox("RAM (in GB)", [2, 4, 6, 8, 12, 16, 24, 32, 64])
weight = st.number_input("Weight (in Kg)", min_value=0.5, max_value=5.0, step=0.1)
touchscreen = st.selectbox("Touchscreen", ['No', 'Yes'])
ips = st.selectbox("IPS Panel", ['No', 'Yes'])
cpu = st.selectbox("CPU Brand", ['Intel Core i3', 'Intel Core i5', 'Intel Core i7', 'AMD Ryzen 5', 'Other Intel Processor'])
hdd = st.selectbox("HDD (in GB)", [0, 128, 256, 512, 1000, 2000])
ssd = st.selectbox("SSD (in GB)", [0, 128, 256, 512, 1024])
gpu = st.selectbox("GPU Brand", ['Intel', 'Nvidia', 'AMD'])
os = st.selectbox("Operating System", ['Windows', 'Mac', 'Others/No OS/Linux'])

# Convert string Yes/No to binary
touchscreen = 1 if touchscreen == 'Yes' else 0
ips = 1 if ips == 'Yes' else 0

# Prepare the input as DataFrame
query = pd.DataFrame([[
    company, typename, ram, weight, touchscreen,
    ips, cpu, hdd, ssd, gpu, os
]], columns=[
    'Company', 'TypeName', 'Ram', 'Weight', 'Touchscreen',
    'Ips', 'Cpu brand', 'HDD', 'SSD', 'Gpu brand', 'os'
])

# Predict button
if st.button("Predict Price"):
    prediction = pipe.predict(query)[0]
    final_price = np.exp(prediction)  # If your model was trained on log(price)
    st.success(f"💰 The predicted price is ₹ {int(final_price):,}")
