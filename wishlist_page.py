import streamlit as st
from helpers import connect_to_deta, fetch_data

def wishlist_page():
    db_user_books_wishlist = connect_to_deta(f'user-{st.session_state.user_name}-wishlist')

    placeholder = st.empty()

    with placeholder.form('form'):
        st.write('Add books to your wishlist here! :)')
        st.write(
            'Again, you can put in as much (or as little) information as you want. But a name would be helpful!')
        book = st.text_input('Your book you want to have')
        author = st.text_input('The author of the book')
        image = st.text_input('Add a link to the cover')
        submitted = st.form_submit_button('Save book 📖')
        close = st.form_submit_button('Close form ❌')

    if submitted:
        db_user_books_wishlist.put({'book': book, 'author': author, 'image': image})

    if close:
        placeholder.empty()

    st.write('Your wishlist:')

    user_wished_books = fetch_data(db_user_books_wishlist)
    st.dataframe(user_wished_books, use_container_width=True, column_order=("image", "book", "author"), hide_index=True,
                 column_config={"image": st.column_config.ImageColumn()}
                 )