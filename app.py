import streamlit as st
from src.bookwish import bookwish_app
from src.helpers import connect_to_deta, fetch_data #importing some predefined functions

#code to configure the page
st.set_page_config(
    page_title='Book Wish',
    page_icon='📖',
    layout='wide'
)

#LOGIN PAGE
placeholder = st.empty()
credentials_check = False

if 'count' not in st.session_state:
    st.session_state.count = 0

db_login = connect_to_deta('bookwish') #connecting to the database that contains the usernames and passwords

#cheking whether the user was logged in before getting to this page
if st.session_state.count == 0:
    #creating a login page
    with placeholder.form('Login'):
        st.markdown('Enter your user information')
        st.session_state.user_name = st.text_input('Username', placeholder='Please enter your user username').lower()
        password = st.text_input('Password', placeholder='Please enter your password', type='password')
        login_button = st.form_submit_button('Login')

        if login_button:
            #fetch the user data
            user_data = fetch_data(db_login)  #fetching the user data
            user_names = list(user_data.user_name)  #list with the usernames from the column user_name

            #if user name exists in user name - go to next site
            if st.session_state.user_name in user_names: #used code from Towards Data Science and Streamlit library
                credentials_check = True
            else:
                st.error('Please provide correct user name')

    if credentials_check == True:
        placeholder.empty() #deleting the login form
        st.session_state.count = 1

#letting the user continue to another page
if st.session_state.count > 0:
    menu = ['Homepage', 'My Books', 'Wishlist', 'My Friends', 'About']
    choice = st.sidebar.selectbox('Menu', menu)
    bookwish_app(choice)