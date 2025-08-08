import streamlit as st
import pandas as pd
from PIL import Image

# data=pd.read_csv("C:\\Users\\Sri\\Downloads\\Iris.csv")
st.title("Voting User Profile")
check=st.checkbox("Click here to upload picture")
if check:
    im=st.sidebar.file_uploader("Upload file",type=("jpg","png","jpeg"))
    if im:
        i=Image.open(im).convert("RGB")
        
name=st.sidebar.text_input("Enter the name")
age=st.sidebar.slider("Enter age",0,70)#4 parameters
# rad=st.sidebar.radio("Gender",("Male","Female"))
add=st.sidebar.text_input("Enter address")
ph=st.sidebar.text_input("Enter phone number")
sub=st.sidebar.button("Submit")
if sub:
    st.write(name)
    st.write(age)
    # st.write(rad)
    st.write(add)
    if not(ph.isdigit() and len(ph)==10):
        st.write("Invalid phone no")
    else:
        st.write(ph) 
    

# file=st.file_uploader("Upload file",type=("csv","xlsx"))
# if file:
#     data=pd.read_csv(file)
#     st.dataframe(data)

