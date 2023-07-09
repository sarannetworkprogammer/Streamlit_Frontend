import streamlit as st

import time as t

#creating
#st.image("image1.png")



# title - it is used to add the title of an app
st.title("Welcome to firstapp ")

# Header
st.header("Machine learning")

# subheader
st.subheader("Linear Regression")

#to give information
st.info("information details of usesr")

#warning message

st.warning("Come on time or else you will be marked absent")

#Error
st.error("wrong password")

#Success message

st.success("Congrats you are passed")

#write

st.write("Employee name")
st.write(range(50))

# Markdown 
st.markdown("# Intellipat")
st.markdown("## Intellipat")
st.markdown("### Intellipat")
st.markdown(":moon:")

st.text("intellipat learners")

#To write a caption

st.caption("caption is here")


#to display mathematical equation

st.latex(r''' a+b x^2+c ''')

#widget

#checkbox
st.checkbox('Login')

#button

st.button("Click ")

#Radio widget

st.radio("pick your gender", ["male", "Female", "other"])

#selectbox

st.selectbox("pick your course",["ML","Cloud"])

#multi select

st.multiselect("choose the dept",["Marketing", "sales"])

#select slider

st.select_slider("Rating",["Bad","Good","Excellent", "Outstanding"])

#Slider

st.slider("Enter ur number", 0,100)

#number_input

st.number_input("pick a number", 0,100)

#text_input

st.text_input("Enter your email address")

#date_input

st.date_input("opening cermony")

#time input

st.time_input("Hey what the timing")

#text area Description, Reason 

st.text_area("welcome to website Hello learners")

#file upload

st.file_uploader("Upload your file/folder")

#colorpicker

st.color_picker("color")

#progress

st.progress(40)

#spinner

with st.spinner("Just Wait"):
    t.sleep(2)

#ballon

st.balloons()

#side bar

st.sidebar.title("welcome to Intellipat")
st.sidebar.text_input("Mail Address")
st.sidebar.text_input("password")
st.sidebar.button("Submit")
st.sidebar.radio("Professional Expert", ["student","working","Others"])



#Data visualization

import pandas as pd 
import numpy as np


# Bar chart
st.title("Barchart")

data = pd.DataFrame(np.random.randn(50,2), columns=["x","y"])
st.bar_chart(data)
# Line chart

st.title("Line chart")

st.line_chart(data)

# Area chart 

st.title("Area chart")
st.area_chart(data)
