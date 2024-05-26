import base64
import streamlit as st
import pickle
import random
import pandas as pd
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

with open("model.pkl",'rb') as f:
    model = pickle.load(f)

img = get_img_as_base64("background.png")
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{img}");
width: 100%;
height:100%
background-repeat: no-repeat;
background-attachment: fixed;
background-size: cover;
}}

[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""


st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown("""
    # *Customer Churn Prediction*            
""")

#Form data
col1, col2, col3 = st.columns(3)
with col1:
   tenure = st.number_input('Tenure')
with col2:
    PreferredLoginDevice = st.selectbox("PreferredLoginDevice", ("Mobile Phone", "Computer"))

with col3:
   CityTier =  st.selectbox("CityTier", (1, 2, 3))

col4, col5, col6 = st.columns(3)
with col4:
    WarehouseToHome = st.number_input('WarehouseToHome')
with col5:
   PreferredPaymentMode =  st.selectbox('PreferredPaymentMode', ('Credit Card', 'Debit Card', 'Cash on Delivery', 'UPI', 'E wallet'))
with col6:
    Sex = st.selectbox('Gender', ('Male', 'Female'))
col7, col8, col9 = st.columns(3)
with col7:
    HourSpendOnApp = st.number_input('HourSpendOnApp')
with col8:
    NumberOfDeviceRegistered = st.number_input('NumberOfDeviceRegistered')
with col9:
   PreferedOrderCat =  st.selectbox('PreferedOrderCat', ('Fashion', 'Laptop & Accessory', 'Mobile Phone'))

col10, col11, col12 = st.columns(3)
with col10:
    SatisfactionScore = st.selectbox('SatisfactionScore', (1, 2, 3, 4, 5))
with col11:
   MaritalStatus =  st.selectbox('MaritalStatus',('Married', 'Single', 'Divorced'))
with col12:
    NumberOfAddress = st.number_input('NumberOfAddress')

col13, col14, col15 = st.columns(3)
with col13:
   Complain =  st.selectbox('Complain',(0, 1))
with col14:
    OrderAmountHikeFromlastYear = st.number_input('OrderAmountHikeFromlastYear')
with col15:
   CouponUsed = st.number_input('CouponUsed')

col16, col17, col18 = st.columns(3)
with col16:
    OrderCount = st.number_input('OrderCount')
with col17:
   DaySinceLastOrder = st.number_input('DaySinceLastOrder')
with col18:
    CashbackAmount = st.number_input('CashbackAmount')

# prediction button
if st.button('Prediction'):

    PreferredLoginDevice = 0
    if PreferredLoginDevice == "Mobile Phone":
        PreferredLoginDevice = 1
    elif PreferredLoginDevice == "Computer":
        PreferredLoginDevice = 2
    
    PreferredPaymentMode = 0
    if PreferredPaymentMode == 'Credit Card':
        PreferredPaymentMode = 1
    if PreferredPaymentMode == 'Debit Card':
        PreferredPaymentMode = 2
    if PreferredPaymentMode == 'Cash on Delivery':
        PreferredPaymentMode = 3
    if PreferredPaymentMode == 'UPI':
        PreferredPaymentMode = 4
    if PreferredPaymentMode == 'E wallet':
        PreferredPaymentMode = 5

    gender = 1
    if Sex=="Female":
        gender=0

    PreferedOrderCat = 0
    if PreferedOrderCat == 'Fashion':
        PreferedOrderCat = 1
    elif  PreferedOrderCat == 'Laptop & Accessory':
        PreferedOrderCat = 2
    elif  PreferedOrderCat == 'Mobile Phone':
        PreferedOrderCat = 3

    MaritalStatus = 0
    if MaritalStatus == "Married":
        MaritalStatus = 1
    elif MaritalStatus == "Single":
        MaritalStatus = 2
    elif MaritalStatus == "Divorced":
        MaritalStatus = 3
    
    #prediction
    result = model.predict([[tenure,PreferredLoginDevice,CityTier, WarehouseToHome,PreferredPaymentMode,
    gender, HourSpendOnApp,NumberOfDeviceRegistered,PreferedOrderCat,SatisfactionScore,
    MaritalStatus, NumberOfAddress, Complain, OrderAmountHikeFromlastYear,CouponUsed,
    OrderCount, DaySinceLastOrder,CashbackAmount]])

    output_labels = {1: "Customer will Churn",
                     0: "Customer will not Churn"}

    st.markdown(f"## {output_labels[result[0]]}")
