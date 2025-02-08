import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the trained model and dataset
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

st.title("Laptop Price Predictor")

# Brand selection
company = st.selectbox('Brand', df['Company'].unique())

# Type of laptop
laptop_type = st.selectbox('Type', df['TypeName'].unique())

# RAM selection
ram = st.selectbox('RAM (in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])

# Laptop weight
weight = st.number_input('Weight of the Laptop')

# Touchscreen
touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])
touchscreen = 1 if touchscreen == 'Yes' else 0

# IPS Panel
ips = st.selectbox('IPS', ['No', 'Yes'])
ips = 1 if ips == 'Yes' else 0

# Screen Size
screen_size = st.slider('Screen Size (in inches)', 10.0, 18.0, 13.0)

# Screen Resolution
resolution = st.selectbox(
    'Screen Resolution', 
    ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', 
     '2880x1800', '2560x1600', '2560x1440', '2304x1440']
)

# Extract resolution values
X_res, Y_res = map(int, resolution.split('x'))
ppi = ((X_res ** 2) + (Y_res ** 2)) ** 0.5 / screen_size

# CPU Selection
cpu = st.selectbox('CPU', df['Cpu brand'].unique())

# HDD & SSD Selection
hdd = st.selectbox('HDD (in GB)', [0, 128, 256, 512, 1024, 2048])
ssd = st.selectbox('SSD (in GB)', [0, 8, 128, 256, 512, 1024])

# GPU Selection
gpu = st.selectbox('GPU', df['Gpu brand'].unique())

# OS Selection
os = st.selectbox('Operating System', df['os'].unique())

# Predict Price Button
if st.button('Predict Price'):
    # Create a DataFrame for input features
    query_df = pd.DataFrame(
        [[company, laptop_type, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os]], 
        columns=['Company', 'TypeName', 'Ram', 'Weight', 'Touchscreen', 'IPS', 'PPI', 
                 'Cpu brand', 'HDD', 'SSD', 'Gpu brand', 'os']
    )

    # Ensure query_df has the same features as the model
    query_df = query_df.reindex(columns=pipe.feature_names_in_, fill_value=0)

    # Predict price
    predicted_price = pipe.predict(query_df)

    # Handle log transformation if applied during training
    predicted_price = np.exp(predicted_price[0]) if predicted_price[0] < 50 else predicted_price[0]

    # Display result
    st.title(f"The predicted price of this configuration is ₹{int(predicted_price)}")
