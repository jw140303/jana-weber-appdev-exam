import streamlit as st
from src.helpers import connect_to_deta, fetch_data

def my_books_page():
    """
    This function creates the My Books page.
    On this page the user can view their saved books and add new books.
    """
    #connecting to the database that contains the books that are specific to the user
    db_user_books = connect_to_deta(f'user-{st.session_state.user_name}')

    placeholder = st.empty()

    #creeating a form to add new books to the database
    with placeholder.form('form'):
        st.write('Add new books here! :)')
        st.write(
            'Remember, you can put in as much (or as little) information as you want. But a name would be helpful!')
        book = st.text_input('Your new book')
        author = st.text_input('The author of the book')
        image = st.text_input('Add a link to the cover')
        rating = st.text_input('What would you rate the book from 1 - 10?')
        submitted = st.form_submit_button('Save book 📖')
        close = st.form_submit_button('Close form ❌')

    if submitted:
        db_user_books.put({'book': book, 'author': author, 'image': image, 'rating': rating}) #add the book to the database

    if close:
        placeholder.empty() #closing the form

    user_owned_books = fetch_data(db_user_books)
    #displaying the users books on the page
    st.dataframe(user_owned_books, use_container_width=True, column_order=("image", "book", "author", "rating"), hide_index=True,
                 column_config={"image": st.column_config.ImageColumn()}
                 )

