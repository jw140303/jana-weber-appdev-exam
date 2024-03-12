import streamlit as st
import random
from PIL import Image

def homepage():
    st.write(f'Welcome back to Book Wish, {st.session_state.user_name}! ✨')

    #displaying the users profile picture
    profile_picture = Image.open(f'images/user-{st.session_state.user_name}-profile-picture.png')
    st.image(profile_picture, width=300)

    #defining quotes for the homepage
    quotes = ['Reading a book a day, keeps the doctor away!', 'Brighten someones day - buy a book!',
              'Book Wish - All your book needs in one place!', 'Brighten someones day with the help of Book Wish!']
    #placing a randomized quote on the homepage
    daily_quote = random.choice(quotes)
    st.write(f'{daily_quote}')

    st.write('Feel free to add new books to your owned books or your wishlist. Also check out your friends!')
