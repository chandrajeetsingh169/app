import streamlit as st

# ...existing code...

# Display a popup welcome message using Streamlit's info box
if "welcome_shown" not in st.session_state:
    st.session_state["welcome_shown"] = True
    st.info("👋 **Welcome!**\n\nThanks for visiting!")
st.text("please select number by +/- or write and then press enter")
st.title("calculator app")
m=st.subheader("this is a simple calculator app")
st.write("you can add, subtract, multiply and divide two numbers")
st.divider()
st.subheader("enter number: ")
a=st.number_input("first number",min_value=0.0)
b=st.number_input("second number",min_value=0.0)
d=st.selectbox("select any operation on number",["+","-","*","/"])
c=st.button("calculate")
st.divider()
z=a+b
if c :
 st.write("please fill value")
 if d=="+":
  z=a+b
elif d=="-":
 z=a-b
elif d=="*":
 z=a*b
elif d=="/":
 if b==0:
  z=0
  
 elif b!=0:
  z=a/b
if c:
 if a and b and c:
  st.write("result is: ",z)
elif a or b or c:
 st.write("result is: ",z)
# Footer for the Streamlit app
import streamlit.components.v1 as components

components.html(
    """
    <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f1f1f1;
            text-align: center;
        }
    </style>
    <div class="footer">
        <p>Made with ❤️ for you</p>
    </div>
    """,
    
    height=100,
)
