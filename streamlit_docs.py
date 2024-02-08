import streamlit as st
import pandas as pd
import time
st.title("Startup Dashboard") # to set the title to our website 
st.header("I am learning streamlit") # to add header 
st.subheader("I am loving it ") # to addd sub-header 
st.write("Hello Mayur , Welcome to the streamlit") # to write text data
st.markdown("""
### My Favourite Movies 
- Race 3
- Humshakals
- Housefull""")

# we can even display our code into it 
st.code("""
def foo(input):
    return foo**2

""")


# Latex
st.latex("""
x^2+2x+b

""")


# dataframe 
df = pd.DataFrame({
"name":["mayur","aryan","aditya"],
"marks":[50,60,70],
"Package":[10,12,14]
})
st.dataframe(df)

# Metric
st.metric("Revenue","RS 3L" ,"3%")

# json 
st.json({
"name":["mayur","aryan","aditya"],
"marks":[50,60,70],
"Package":[10,12,14]
})


# How to display media (Images , videos , audio and that all)
st.image("My formal pic.png")
#st.video("name of the video file")
#st.audio("name of the audio file ")

# side by side image 
col1,col2 = st.columns(2)
with col1:
    st.image("my formal pic.png")
with col2:
    st.image("my formal pic.png")


#sidebar
st.sidebar.title("MY SIDEBAR")


#SHOWING STATUS
st.error("LOGIN FAILED")
st.success("LOGIN SUCCESSFULL")
st.info("INFORMATION")
st.warning("DANGER")


# PROGRESSBAR
bar  = st.progress(0)
for i in range(100):
    time.sleep(0.1)
    bar.progress(i)


# TAKING USER INPUT 
#1) Text input
email = st.text_input("Enter Email")

#2) number input
num = st.number_input("Enter numbers :")

#3) date input
date = st.date_input("Enter current date :")



# BUTTON & DROPDOWN



email = st.text_input("Enter the text ;")
password = st.text_input("Enter the password")
gender = st.selectbox("select gender" ,["male","female","gender"])


btn = st.button("LOGIN")
# if the button is clicked 
if btn: # it means jevha mi button vr click karel tevha ch ha vala block run vyayala pahije 

    if email=="mayur" and password=="1234":
        st.success("LOGIN SUCESSFUL")
        st.balloons() # to pop up the ballons on the screen
        st.write(gender)
    else:
        st.error("LOGIN FAILED......")


        
# how to upload any file 

file = st.file_uploader("csv file")
if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.describe)