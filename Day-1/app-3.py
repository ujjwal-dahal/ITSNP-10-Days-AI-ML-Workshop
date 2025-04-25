
import streamlit as st 
import matplotlib.pyplot as plt


#title
st.title("Data Visualization")

#Dictionary
data = {
  "Apple" : 50,
  "Grapes" : 60,
  "Banana" : 100
}

#Displaying Dictionary
st.write("Fruit Inventory : ",data)


#update dictionary

key = st.text_input("Enter New Key : ")
value = st.text_input("Enter Integer Value for That key : ")

if st.button("Update Dictionary"):
  if key and value:
    data[key]= int(value);
    
    st.write("Updated Dictionary is : ",data)
    
#Bar Chart Plot garna

st.header("Bar Chart of Frtuits Inventory is : ")
fig , ax= plt.subplots() 
ax.bar(data.keys(),data.values())
ax.set_xlabel("Fruits")
ax.set_ylabel("Quantity")
st.pyplot(fig)
