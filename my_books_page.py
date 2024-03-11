import streamlit as st
from helpers import connect_to_deta, fetch_data

def my_books_page():
    db_user_books = connect_to_deta(f'user-{st.session_state.user_name}')

    placeholder = st.empty()

    with placeholder.form('form'):
        st.write('Add new books here! :)')
        st.write(
            'Remember, you can put in as much (or as little) information as you want. But a name would be helpful!')
        book = st.text_input('Your new book')
        author = st.text_input('The author of the book')
        image = st.text_input('Add a link to the cover')
        submitted = st.form_submit_button('Save book 📖')
        close = st.form_submit_button('Close form ❌')

    if submitted:
        db_user_books.put({'book': book, 'author': author, 'image': image})

    if close:
        placeholder.empty()

    st.write('Your books:')

    user_owned_books = fetch_data(db_user_books)
    st.dataframe(user_owned_books, use_container_width=True, column_order=("image", "book", "author"), hide_index=True,
                 column_config={"image": st.column_config.ImageColumn()}
                 )

