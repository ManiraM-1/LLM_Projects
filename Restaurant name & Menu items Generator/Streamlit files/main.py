import streamlit as st
import langchain_helper

st.title("Restaurant Name & Menu Generator")

cuisine = st.sidebar.selectbox("Select a Cuisine",("Indian","Italian","Mexian","American","Korean","Chinese","Arabian"))



if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    # here strip() removes the leading and ending white spaces and unnecessary characters
    st.write("**Menu-items**")
    for item in menu_items:
        st.write("-",item)
