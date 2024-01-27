import streamlit as st
header = st.header("Your Personal Information:")
name = st.text_input("Enter your name:")
uname = st.text_input("Enter your University Name:")
ex = st.text_area("Enter your Expectations:")
class_data = st.selectbox("Select Semester:", (1, 2, 3, 4))

button = st.button("Done")  
if button:
    st.markdown(f"""
     Name : {name}
     University Name : {uname}
     Expectation : {ex}
     Class data : {class_data}
     """)
