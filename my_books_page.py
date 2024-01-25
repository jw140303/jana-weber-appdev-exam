import streamlit as st
from helpers import connect_to_deta, fetch_data

def my_books_page():
    db_test_books = connect_to_deta('user-test')

    add_books = st.button('Add something to your list!')

    #if add_books: #does not work, make it make sense pls uwu?!

    with st.form('form'):
        st.write('Remember, you can put in as much (or as little) information as you want. But a name would be helpful!')
        book = st.text_input('Your new book')
        author = st.text_input('The author of the book')
        image = st.text_input('Add a link to the cover')
        submitted = st.form_submit_button('Save book 📖')
        close = st.form_submit_button('Close form ❌')

    if submitted:
        db_test_books.put({'book': book, 'author': author, 'image': image})

    if close:
        my_books_page()

    st.write('Your books:')

    test_owned_books = fetch_data(db_test_books)
    st.dataframe(test_owned_books, use_container_width=True, column_order=("image", "book", "author"), hide_index=True,
                 column_config={"image": st.column_config.ImageColumn()}
                 )
