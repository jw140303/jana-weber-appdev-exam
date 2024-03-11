import streamlit as st
import random
from PIL import Image

def homepage():
    c1, c2 = st.columns(2)  # creating two columns to separate the page

    with c1:

        st.write(f'Welcome back to Book Wish, {st.session_state.user_name}! ✨') #used code from Towards Data Science and Streamlit library

        #defining quotes for the homepage
        quotes = ['Reading a book a day, keeps the doctor away!', 'Brighten someones day - buy a book!']
        #placing a randomized quote on the homepage
        daily_quote = random.choice(quotes)
        st.write(f'{daily_quote}')

    with c2:

        #displaying the users profile on the right side of the page
        profile_picture = Image.open(f'images/user-{st.session_state.user_name}-profile-picture.png')
        st.image(profile_picture)

        new_profile_picture = st.file_uploader('Change profile picture:',
                                               type=['jpg', 'png', 'jpeg'])
        if new_profile_picture is not None:
            pass #continue this
