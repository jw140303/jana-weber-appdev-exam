import streamlit as st
from homepage import homepage
from my_books_page import my_books_page

def bookwish_app(choice):
    #LAUNCHING THE APP
    #creating a menu bar

    if choice == 'Homepage':
        st.subheader('Home')
        homepage()
    elif choice == 'My Books':
        st.subheader('My owned books')
        my_books_page()
    elif choice == 'Wishlist':
        st.subheader('My Book Wishlist')
    elif choice == 'My Friends':
        st.subheader('My Friends')
    elif choice == 'About':
        st.subheader('About')
        st.write('✨ Hi, Im Jana. I created this MVP for university.. Hope you enjoy! ✨')