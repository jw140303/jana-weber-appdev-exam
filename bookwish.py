import streamlit as st
from homepage import homepage
from my_books_page import my_books_page
from wishlist_page import wishlist_page
from friends_page import friends_page

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
        wishlist_page()
    elif choice == 'My Friends':
        st.subheader('My Friends')
        friends_page()
    elif choice == 'About':
        st.subheader('About')
        st.write('✨ Hi, Im Jana. I created this Bookwish MVP as my exam project for a seminar at my university. ✨')
        st.write('The first idea was to create a space to save all the books you have and want to have, '
                 'so you do not have to remember every single one. However, it has evolved to be more social! '
                 'Bookwish is all about sharing your love of books with your friends and making and receiving gifts. '
                 'In future you will be able to talk about your favourite (or least favourite) books, write reviews and more. ')