import streamlit as st

def my_books_page():
    st.write('Here you can see your books!')
    st.write('Do you want to add a book??')

    #creating an empty lists with books
    owned_books = []

    new_book = st.text_input('Enter the book name here!')
    owned_books.append(new_book)

    print(owned_books)