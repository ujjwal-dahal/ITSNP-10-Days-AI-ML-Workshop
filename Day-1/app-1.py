

import streamlit as st 

#Title Adding
st.title("My First Streamlit App")


#Display Text
st.write("Welcome to my streamlit app")

#Button add garna
st.button("Click Me") #Esle either True dincha or False dincha user le click garda

returnValue = st.button("Again Click Me For Checking")
if returnValue:
  st.write("You have clicked me")
  
  returnValue = False

if returnValue==False:
  st.write("You have unclicked me")
  