import streamlit as st
import random

def homepage():
    st.write('Welcome back to Book Wish! ✨')

    #defining quotes for the homepage
    quotes = ['Reading a book a day, keeps the doctor away!', 'Brighten someones day - buy a book!']
    #placing a randomized quote on the homepage
    daily_quote = random.choice(quotes)
    st.write(f'{daily_quote}')