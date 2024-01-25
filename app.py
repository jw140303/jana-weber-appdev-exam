import streamlit as st
from bookwish import bookwish_app
from helpers import connect_to_deta, fetch_data

# code to configure the page
st.set_page_config(
    page_title='Book Wish',
    page_icon='📖',
    layout='wide'
)

# LOGIN PAGE
placeholder = st.empty()
credentials_check = False

db = connect_to_deta('bookwish')

with placeholder.form('Login'):
    st.markdown('Enter your user information')
    user_name = st.text_input('Username', placeholder='Please enter your user username').lower()
    password = st.text_input('Password', placeholder='Please enter your password', type='password')
    login_button = st.form_submit_button('Login')

    if login_button:
        # fetch the user data
        user_data = fetch_data(db)  # fetching all the data I stored on my user
        user_names = list(user_data.user_name)  # list with the user names from the column user_name

        # if user name exists in user name - go to next site
        if user_name in user_names:
            credentials_check = True
        else:
            st.error('Please provide correct user name')

if credentials_check == True:
    # delete the form widgets
    placeholder.empty()

    bookwish_app()