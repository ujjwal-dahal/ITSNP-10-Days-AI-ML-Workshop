
import streamlit as st 

#title rakheko
st.title("This is Streamlit Title")

#Creating List
st.header("We are creating a List")
fruits = ["mango","grapes","coconut"]

st.write("Original List is : ",fruits)

#text box banaune
new_fruit = st.text_input("Fruits Add Gara : ")
if st.button("Add Fruit"):
    if new_fruit:
      fruits.append(new_fruit)
      st.write("Updated List : ",fruits)
    

