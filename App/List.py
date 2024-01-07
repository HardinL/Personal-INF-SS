import streamlit as st
import pandas as pd
import numpy as np
import mysql.connector



if "open_table" not in st.session_state:
    st.session_state["open_table"] = False



# connect python with mysql with your hostname,  
# username, password and database 
db = mysql.connector.connect(user = "root", password = "20020205", database = "list") 
  
# get cursor object 
cursor= db.cursor() 
  
# execute your query 
cursor.execute("SELECT * FROM person") 
  
# fetch all the matching rows  
result = cursor.fetchall() 

st.markdown("# List")

# Add tabs
# tab1, tab2 = st.tabs(["Display", "Something Else"])

# searched_item = None

# Read from database
# table = pd.read_csv("data.csv")
table = pd.DataFrame(result, columns = ['Name', 'Gender', 'Date of Birth', 'Height', 'Weight', 'Marriage Situation', 'Education', 'Salary', 'Address'])
table.index = np.arange(1, len(table)+1)    # Set index to start from 1




if st.button("SELECT"):
    st.session_state["open_table"] = True



if st.session_state["open_table"]:
    df_with_selections = table.copy()
    df_with_selections.insert(0, "Select", False)
    edited_df = st.data_editor(
        df_with_selections,
        column_config={"Select": st.column_config.CheckboxColumn(required=True)},
        disabled=table.columns
    )
else:
    st.write(table)



if st.button("CANCEL") and st.session_state["open_table"] == True:
    st.session_state["open_table"] = False




# if st.button("SELECT"):
#     table.insert(0, "Select", False)
    
# st.write(table)



with st.sidebar:
    st.markdown("# List")
    st.text("Number of person: ")
    st.text(len(table))

# with st.sidebar:
#     st.title("Insert")

#     name = st.text_input("Name")
#     age = st.text_input("Age")
#     person_id = st.text_input("ID")
#     salary = st.number_input("Salary")


#     if st.button("Insert"):
#         data_to_add = {
#             "Name": name, 
#             "Age": age, 
#             "ID": person_id, 
#             "Salary": salary
#             }

#         new_row = pd.DataFrame(data_to_add, index=[0])
#         table = pd.concat([table, new_row], ignore_index=True)

#         # Save to database
#         table.to_csv("data.csv", index=False)


#     st.title("Delete")

#     # Delete by index
#     index = st.text_input("Index")

#     if st.button("Delete"):
#         table = table.drop(index=index)

#         # Save to database
#         table.to_csv("data.csv", index=False)


#     st.title("Search")

#     # ID search
#     sid = st.text_input("Search ID")

#     if st.button("Search"):
#         searched_item = table[table["ID"] == int(sid)]


    


# with tab1:
#     st.title("Main")




# with tab2:
#     st.title("Something Else")

#     if searched_item is not None:
#         st.table(searched_item)

