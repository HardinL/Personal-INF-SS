import streamlit as st
import mysql.connector

# connect python with mysql with your hostname,  
# username, password and database 
db= mysql.connector.connect(user = "root", password = "20020205", database = "list") 
  
# get cursor object 
cursor= db.cursor() 

st.markdown("# Search")

with st.sidebar:
    st.markdown("# Conditions")
    name = st.text_input("Name:")
    gender = st.selectbox("Gender", ["All gender","Female", "Male", "Non-binary", "Prefer not to say"])

    col1, col2 = st.columns(2)
    
    with col1: 
        min_dob = 
    


