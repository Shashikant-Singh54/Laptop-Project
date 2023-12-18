import numpy as np
import streamlit as st
import pickle
import sklearn

laptop: object = pickle.load(open('laptop.pkl','rb'))
pipe = pickle.load(open('pipe3.pkl','rb'))

st.title("Laptop Predictor")
st.image('OIP.jfif',  width=300)
IPS = st.selectbox('IPS', ['Yes','No'])

TouchScreen = st.selectbox('TouchScreen', ['Yes','No'])
# Brand
Company = st.selectbox('Brand', laptop['Company'].unique())
# typename
TypeName = st.selectbox('TypeName', laptop['TypeName'].unique())
Inches = st.selectbox('Inches', laptop['Inches'].unique())
Ram = st.selectbox('Ram', [ 8, 16,  4,  2, 12, 64,  6, 32, 24,1])
graphic_processor = st.selectbox('graphic_Type', laptop['graphic_processor'].unique())
Gpu = st.selectbox('Gpu', laptop['Gpu'].unique())
GHz = st.selectbox('GHz', laptop['GHz'].unique())

OpSys = st.selectbox('Operating_System', laptop['OpSys'].unique())
Weight = st.selectbox('Weight', laptop['Weight'].unique())



Flash_Storage = st.selectbox('Flash_Storage', laptop['Flash_Storage'].unique())

SSD1 = st.selectbox('SSD', laptop['SSD1'].unique())

HDD1 = st.selectbox('HDD', laptop['HDD1'].unique())

HYBRID1 = st.selectbox('HYBRID', laptop['HYBRID1'].unique())

Resolution = st.selectbox('PPi', ['2560x1600', '1440x900', '1920x1080', '2880x1800', '1366x768',
       '2304x1440', '3200x1800', '2256x1504', '3840x2160', '2160x1440',
       '1600x900', '2560x1440', '2736x1824', '2400x1600', '1920x1200'])

if st.button('Prtedict Price'):



    x_res = Resolution.split('x')[0]
    y_res = Resolution.split('x')[1]
    x_res = int(x_res)
    y_res = int(y_res)
    Inches = float(Inches)

    PPI = ((x_res**2) + (y_res**2)) / Inches

    if TouchScreen == 'Yes':
        TouchScreen = 1
    else:
        TouchScreen = 0

    if IPS == 'Yes':
        IPS = 1
    else:
        IPS = 0


    query = np.array([IPS,TouchScreen,Company,TypeName,Inches,Ram,graphic_processor, Gpu, GHz, OpSys, Weight, Flash_Storage, SSD1, HDD1, HYBRID1,PPI])

    query = query.reshape(1,16)



    st.title(pipe.predict(query))

