import streamlit as st
import pandas as pd
import numpy as np

def main_page():
    st.markdown("List")
    st.sidebar.markdown("List")

# Add tabs
# tab1, tab2 = st.tabs(["Display", "Something Else"])

# searched_item = None

# Read from database
table = pd.read_csv("data.csv")
table.index = np.arange(1, len(table)+1)    # Set index to start from 1


with st.sidebar:
    st.title("Insert")

    name = st.text_input("Name")
    age = st.text_input("Age")
    person_id = st.text_input("ID")
    salary = st.number_input("Salary")


    if st.button("Insert"):
        data_to_add = {
            "Name": name, 
            "Age": age, 
            "ID": person_id, 
            "Salary": salary
            }

        new_row = pd.DataFrame(data_to_add, index=[0])
        table = pd.concat([table, new_row], ignore_index=True)

        # Save to database
        table.to_csv("data.csv", index=False)


    st.title("Delete")

    # Delete by index
    index = st.text_input("Index")

    if st.button("Delete"):
        table = table.drop(index=index)

        # Save to database
        table.to_csv("data.csv", index=False)


    st.title("Search")

    # ID search
    sid = st.text_input("Search ID")

    if st.button("Search"):
        searched_item = table[table["ID"] == int(sid)]


    


# with tab1:
#     st.title("Main")

#     # Show table
#     st.table(table)




# with tab2:
#     st.title("Something Else")

#     if searched_item is not None:
#         st.table(searched_item)

