import streamlit as st
from groq import Groq
st.set_page_config(page_title = "Student_Application", page_icon ="👩‍🏫", layout = "centered")
st.title("Student Profile Application ")
st.caption("Developed By LOHITA R PATIL")
st.caption("ℹ️Fill in your and click View My profile")
name = st.text_input("Student Name")
usn = st.text_input("USN/Roll number")
dept = st.selectbox("Department",["CSE", "ISE", "ECE", "EEE", "Mech", "Civil"])
year = st.radio("Current year", ["1st Year", "2nd Year, "3rd Year", "4th Year"])
if st.button("View My Profile"):
    st.subheader("Profile submitted succesfully")

    st.write("Student Name:", name)
    st.write("USN/Roll Number:", usn)
    st.write("Department:", dept)
    st.write("Current Year:", year)
