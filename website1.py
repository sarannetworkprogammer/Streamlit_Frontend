import streamlit as st


# find more emojis

st.set_page_config(page_title ="My Webpage", page_icon = ":tagda:", layout="wide")

#Header section

with st.container():
    st.subheader("Hi, I am sven :wave:")
    st.title("A Data analyst from germany")
    st.write("I am passionate about finding ways to use python and VBA to be more effective")
    st.write("[Learn More >](https://pythonandvba.com)") # Embeding link


# ---------what I do-----------

with st.container():
    st.write("----------")
    left_column,right_column = st.columns(2)

    with left_column:
        st.header("what I do")
        st.write("##")
        st.write(

            """
            On my youtube channel creating tutorials for people who:
            ----are looking for a way to levarage power of python in day to day life
            want to learn data analysis
            """

        )

        st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")   # embeding link inside here 

     



