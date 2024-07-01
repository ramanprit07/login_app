import streamlit as st
import cv2
import numpy as np

# Load logo image
logo_img = cv2.imread('login-logo-png-10.png')

# Create a Streamlit page
st.title("Login Page")
st.markdown("### Welcome to our login page!")

# Create a column for the login form
col1, col2 = st.columns(2)

with col1:
    # Display the logo image
    st.image(logo_img, use_column_width=True)

with col2:
    # Create a form for the login credentials
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Create a login button
    login_button = st.button("Login")

    # Check if the login button is clicked
    if login_button:
        # Verify the login credentials (replace with your own logic)
        if username == "admin" and password == "password":
            st.success("Login successful!")
        else:
            st.error("Invalid username or password")

# Set the GIF as the background image
st.write("""
<style>
body {
    background-image: url("https://media2.giphy.com/media/26BRGoqbUQvk8nwTC/giphy.gif");
    background-size: cover;
    background-position: center;
}
</style>
""", unsafe_allow_html=True)

# Run the app
st.write("Login Page")