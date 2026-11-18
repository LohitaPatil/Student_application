import streamlit as st
from groq import Groq
st.set_page_config(page_title = "Student_Application", page_icon ="👩‍🏫", layout = "centered")
st.title("Student Profile Application ")
st.caption("Developed By LOHITA R PATIL")
st.caption("ℹ️Fill in your and click View My profile")
st.text_input("Student Name")
st.text_input("USN/Roll number)
st.selectbox("Department",["CSE", "ISE", "ECE", "EEE", "Mech", "Civil"])
