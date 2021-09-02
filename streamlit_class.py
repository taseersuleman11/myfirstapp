import streamlit as st


st.button('Click')
check = st.checkbox('Check me out')

st.success("We are succeeded")

#st.sidebar()

#a = st.sidebar.text("Please enter the text")
#st.sidebar.time_input('Time entry')
#st.sidebar.date_input('Date input')

st.color_picker('Pick a color')

st.video("https://www.youtube.com/watch?v=XqZsoesa55w")

st.video("https://www.youtube.com/watch?v=6BN3vCa2U_A")

a = st.sidebar.number_input('Enter first number')
b = st.sidebar.number_input('Enter second number')

if st.sidebar.button("Submit"):

    c = a+b
    st.info("The result of addition is")
    st.sidebar.balloons()
    st.write(c)

