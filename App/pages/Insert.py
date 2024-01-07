import streamlit as st
import mysql.connector

# connect the database
db= mysql.connector.connect(user = "root", password = "20020205", database = "list") 
  
# get cursor object 
cursor= db.cursor() 

st.markdown("# Insert")
st.sidebar.markdown("# Insert")

col1, col2, col3 = st.columns([2,1,1])

with col1:
    name = st.text_input("Name", placeholder="First (Middle) Last")

with col2:
    gender = st.selectbox("Gender", ["","Female", "Male", "Non-binary", "Prefer not to say"])

with col3:
    dob = st.date_input("Date of Birth", value = None)

col4, col5 = st.columns(2)

with col4:
    height = st.number_input("Height", value = None, placeholder="Unit in cm")

with col5:
    weight = st.number_input("Weight", value = None, placeholder="Unit in kg")

married = st.text_input("Marriage Situation", placeholder="Ex: Not married")

col6, col7 = st.columns(2)

with col6:
    education = st.text_input("Education", placeholder="Degrees, Ex: College")

with col7:
    salary = st.number_input("Salary", value = None, placeholder="Annual income")

address = st.text_input("Address", placeholder="State/City")

col8, col9, col10 = st.columns([5,1,5])

with col9:
    if st.button('Add'):
        if not all([name, gender, dob, height, weight, married, education, salary, address]):
            # Display an error message if any field is empty
            st.error("Please fill in all required fields.")
        else:
            insert_query = '''INSERT INTO `person` (`name`, `gender`, `dob`, `height`, `weight`, `married`, `education`, `salary`, `address`) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'''
            cursor.execute(insert_query, (name, gender, dob, height, weight, married, education, salary, address))
            db.commit()

            # Display success message
            st.success("Person is successfully added!")

# fetch all the matching rows  
# result = cursor.fetchall() 

